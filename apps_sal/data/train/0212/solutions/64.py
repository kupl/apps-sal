class Solution:
    def numFactoredBinaryTrees(self, A: List[int]) -> int:
        n = len(A)
        A.sort()
        dp = [1] * n
        mod = 10**9 + 7
        index = {c: i for i, c in enumerate(A)}

        for i, x in enumerate(A):
            for j in range(n):
                if x % A[j] == 0:
                    right = x / A[j]
                    if right in index:
                        dp[i] += dp[j] * dp[index[right]]
                        dp[i] = dp[i] % mod
        return sum(dp) % mod
