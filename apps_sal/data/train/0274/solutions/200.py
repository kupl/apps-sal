class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        maxd = collections.deque()
        mind = collections.deque()

        s, e = 0, 0
        res = 0
        while e < len(nums):
            while len(maxd) and nums[e] >= nums[maxd[-1]]:
                maxd.pop()
            while len(mind) and nums[e] <= nums[mind[-1]]:
                mind.pop()
            maxd.append(e)
            mind.append(e)
            if nums[maxd[0]] - nums[mind[0]] > limit:
                s += 1
                if s > mind[0]:
                    mind.popleft()
                if s > maxd[0]:
                    maxd.popleft()
            else:
                res = max(res, e - s + 1)
                e += 1
        return res
