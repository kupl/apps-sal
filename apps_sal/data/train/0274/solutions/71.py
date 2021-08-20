class Solution:

    def longestSubarray(self, nums: List[int], limit: int) -> int:
        (maxd, mind) = (collections.deque(), collections.deque())
        (l, r, res) = (0, 0, 0)
        while r < len(nums):
            while len(maxd) and maxd[-1] < nums[r]:
                maxd.pop()
            while len(mind) and mind[-1] > nums[r]:
                mind.pop()
            maxd.append(nums[r])
            mind.append(nums[r])
            while maxd[0] - mind[0] > limit:
                if nums[l] == maxd[0]:
                    maxd.popleft()
                if nums[l] == mind[0]:
                    mind.popleft()
                l += 1
            res = max(r - l + 1, res)
            r += 1
        return res
