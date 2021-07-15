class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        walk = {0:-1}
        prefixSum = 0
        delimiter = -1
        res = 0
        for i in range(len(nums)):
            prefixSum += nums[i]
            remain = prefixSum - target
            if (remain in walk.keys() and walk[remain] >= delimiter):
                res += 1
                delimiter = i
            walk[prefixSum] = i
        return res
