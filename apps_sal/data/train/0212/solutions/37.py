class Solution:
    def numFactoredBinaryTrees(self, A):
        MOD = 10 ** 9 + 7
        n = len(A)
        A.sort()
        dp = [1] * n
        index = {x: i for i, x in enumerate(A)}
        for i, x in enumerate(A):
            for j in range(i):
                if x % A[j] == 0:
                    right = x / A[j]
                    if right in index:
                        dp[i] += dp[j] * dp[index[right]]
                        dp[i] %= MOD

        return sum(dp) % MOD
