class Solution:

    def longestSubarray(self, nums: List[int], limit: int) -> int:
        if not nums:
            return 0
        (maxd, mind) = (deque(), deque())
        (res, j) = (0, 0)
        for i in range(len(nums)):
            while len(maxd) > 0 and nums[maxd[-1]] < nums[i]:
                maxd.pop()
            while len(mind) > 0 and nums[mind[-1]] > nums[i]:
                mind.pop()
            maxd.append(i)
            mind.append(i)
            while j < i and len(maxd) > 0 and (len(mind) > 0) and (nums[maxd[0]] - nums[mind[0]] > limit):
                if j == maxd[0]:
                    maxd.popleft()
                if j == mind[0]:
                    mind.popleft()
                j += 1
            res = max(res, i - j + 1)
        return res
