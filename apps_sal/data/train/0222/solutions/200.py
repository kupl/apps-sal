class Solution:

    def lenLongestFibSubseq(self, A: List[int]) -> int:
        n = len(A)
        Aset = set(A)
        ans = 0
        dp = {}
        for i in range(1, n):
            for j in range(i):
                diff = A[i] - A[j]
                if diff < A[j] and diff in Aset:
                    dp[A[j], A[i]] = dp.get((diff, A[j]), 2) + 1
                    ans = max(ans, dp[A[j], A[i]])
        return ans
