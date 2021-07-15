class Solution:
    def numFactoredBinaryTrees(self, A: List[int]) -> int:
        A.sort()
        dp = {}
        res = 0
        for i in range(len(A)):
            dp[A[i]] = 1
            for j in range(i):
                if A[j] * A[j] == A[i]:
                    dp[A[i]] += dp[A[j]] * dp[A[j]]
                    dp[A[i]] %= 1000_000_007
                elif A[j] * A[j] > A[i] and A[i] % A[j] == 0:
                    dp[A[i]] += dp[A[j]] * dp.get(A[i] // A[j], 0) * 2
                    dp[A[i]] %= 1000_000_007
            res += dp[A[i]]
            res %= 1000_000_007
        return res
