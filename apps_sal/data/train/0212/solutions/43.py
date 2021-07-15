class Solution:
    def numFactoredBinaryTrees(self, A: List[int]) -> int:
        if not A:
            return 0

        A.sort()
        dp = {}
        for i in range(len(A)):
            dp[A[i]] = 1
            for j in range(i):
                if A[i] % A[j] == 0 and int(A[i]/A[j]) in dp:
                    dp[A[i]] += dp[A[j]] * dp[A[i]/A[j]]

        result = 0
        for key in dp:
            result += dp[key]

        return result % (10 ** 9 + 7)
