class Solution:

    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        dic = {0: -1}
        acc = 0
        last = -1
        res = 0
        for (i, n) in enumerate(nums):
            acc += n
            if acc - target in dic and dic[acc - target] >= last:
                res += 1
                last = i
            dic[acc] = i
        return res
