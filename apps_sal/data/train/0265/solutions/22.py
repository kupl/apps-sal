class Solution:

    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        m = {0: 0}
        res = 0
        sum = 0
        for x in nums:
            sum += x
            if sum - target in m:
                res = max(res, m[sum - target] + 1)
            m[sum] = res
        return res
