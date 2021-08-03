class Solution:
    def kSimilarity(self, A: str, B: str) -> int:

        def dfs(A, B):
            if not A and not B:
                return 0
            if str(A) == str(B):
                return 0
            k = str(A)
            if k in dp:
                return dp[k]

            dp[k] = len(A) - 1

            if A[0] == B[0]:
                dp[k] = dfs(A[1:], B[1:])
                return dp[k]

            for j in range(1, len(A)):
                if A[j] == B[0]:
                    A[0], A[j] = A[j], A[0]
                    dp[k] = min(dp[k], 1 + dfs(A[1:], B[1:]))
                    A[j], A[0] = A[0], A[j]

            return dp[k]

        dp = dict()
        A, B = list(A), list(B)
        dp[str(A)] = dfs(A, B)

        return dp[str(A)]
