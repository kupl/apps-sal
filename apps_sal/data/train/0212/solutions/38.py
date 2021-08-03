import math


class Solution:
    def numFactoredBinaryTrees(self, A: List[int]) -> int:
        mod = 1000000007
        dp = [1 for i in range(len(A))]
        A.sort()
        val_to_idx = {val: idx for idx, val in enumerate(A)}
        M = len(A)
        for i in range(M):
            for j in range(0, i):

                if A[i] % A[j] == 0 and A[i] // A[j] in val_to_idx:
                    dp[i] += (dp[j] * dp[val_to_idx[A[i] // A[j]]]) % mod
                    dp[i] = dp[i] % mod
        print(dp)
        return sum(dp) % mod
