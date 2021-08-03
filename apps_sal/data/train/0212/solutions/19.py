class Solution:
    def numFactoredBinaryTrees(self, A: List[int]) -> int:
        A.sort()
        d = {A[0]: 0}
        dp = [1] * len(A)
        MOD = 1000000007

        for i in range(1, len(A)):
            for j in range(0, i):
                t = A[i] // A[j]
                if t < A[j]:
                    break

                if not A[i] % A[j] and t in d:
                    if A[j] == t:
                        dp[i] += dp[j] * dp[d[t]]
                    else:
                        dp[i] += dp[j] * dp[d[t]] * 2

            dp[i] %= MOD
            d[A[i]] = i

        return sum(dp) % MOD
