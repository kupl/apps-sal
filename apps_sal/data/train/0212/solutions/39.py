class Solution:
    def numFactoredBinaryTrees(self, A: List[int]) -> int:

        A.sort()
        dp = {val: 1 for val in A}

        for i in range(len(A)):
            for j in range(i):
                if A[i] % A[j] == 0 and A[i] // A[j] in dp:
                    dp[A[i]] += dp[A[i] // A[j]] * dp[A[j]]

        return sum(dp[v] for v in dp) % (10 ** 9 + 7)
