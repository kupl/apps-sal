class Solution:

    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        D = {0: -1}
        cumsum = 0
        idx = -1
        res = 0
        for (i, x) in enumerate(nums):
            cumsum += x
            if cumsum - target in D and D[cumsum - target] >= idx:
                res += 1
                idx = i
            D[cumsum] = i
        return res
