class Solution:

    def numFactoredBinaryTrees(self, A: List[int]) -> int:
        MOD = int(1000000000.0 + 7)
        N = len(A)
        A.sort()
        dp = [1] * N
        idx = {ele: i for (i, ele) in enumerate(A)}
        for (i, root_val) in enumerate(A):
            for j in range(i):
                left = A[j]
                if root_val % left == 0:
                    right = root_val / left
                    if right in idx:
                        dp[i] += dp[j] * dp[idx[right]]
                        dp[i] %= MOD
        return sum(dp) % MOD
