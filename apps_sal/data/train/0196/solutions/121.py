class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        def maxSum(gen):
            res = cur = -float('inf')
            for n in gen:
                cur = n + max(0, cur)
                res = max(res, cur)
            return res

        total = sum(A)
        res1 = maxSum(iter(A))
        res2 = total + maxSum(-A[i] for i in range(1, len(A)))  # min sum of the unwated sub array
        res3 = total + maxSum(-A[i] for i in range(len(A) - 1))
        return max(res1, res2, res3)
