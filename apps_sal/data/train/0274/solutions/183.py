class Solution:

    def longestSubarray(self, nums: List[int], limit: int) -> int:
        maxD = []
        minD = []
        ind = 0
        res = 0
        slow = 0
        fast = 0
        while slow <= fast and fast < len(nums):
            while len(maxD) > 0 and maxD[len(maxD) - 1] < nums[fast]:
                maxD.pop(len(maxD) - 1)
            maxD.append(nums[fast])
            while len(minD) > 0 and minD[len(minD) - 1] > nums[fast]:
                minD.pop(len(minD) - 1)
            minD.append(nums[fast])
            while maxD[0] - minD[0] > limit and slow < fast:
                if maxD[0] == nums[slow]:
                    maxD.pop(0)
                if minD[0] == nums[slow]:
                    minD.pop(0)
                slow += 1
            res = max(res, fast - slow + 1)
            fast += 1
        return res
