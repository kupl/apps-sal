class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        if len(A) == 1:
            return A[0]
        s = sum(A)
        nums = A
        m = nums[0]
        last = m
        num = 1
        last_max = m
        res = last
        res_max = last_max
        for i in A[1:]:
            if i + last < i:
                last = i + last
                num += 1
            else:
                last = i
                num = 1
            if num != len(A):
                res = min(res, last)
            last_max = max(i, i + last_max)
            res_max = max(res_max, last_max)
        return max(s - res, res_max)
