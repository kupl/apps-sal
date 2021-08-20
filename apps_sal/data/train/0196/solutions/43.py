class Solution:

    def maxSubarraySumCircular(self, A: List[int]) -> int:
        for i in range(1, len(A)):
            A[i] += A[i - 1]
        (pre_min, pre_max) = (float('inf'), float('-inf'))
        (res1, res2) = (A[0], A[0])
        for a in A:
            res1 = max(res1, a - pre_min)
            res2 = min(res2, a - pre_max)
            pre_min = min(pre_min, a)
            pre_max = max(pre_max, a)
        res1 = max(res1, A[-1])
        res2 = min(res2, A[-1])
        if res2 == A[-1]:
            return res1
        else:
            return max(res1, A[-1] - res2)
