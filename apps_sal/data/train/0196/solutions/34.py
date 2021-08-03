class Solution:
    def maxSubarraySumCircular(self, A):
        n = len(A)
        S = sum(A)
        m1 = self.kadane(A)
        m2 = S + self.kadane([-A[i] for i in range(1, n)])
        m3 = S + self.kadane([-A[i] for i in range(n - 1)])
        return max(m1, m2, m3)

    def kadane(self, arr):
        res = cur = -float('inf')
        for a in arr:
            cur = a + max(0, cur)
            res = max(cur, res)
        return res
