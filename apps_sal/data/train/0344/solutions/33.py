class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        dp = [1] * len(A[0])
        for j in range(1, len(A[0])):
            for k in range(j):
                isAfter = True
                for i in range(len(A)):
                    if A[i][k] > A[i][j]:
                        isAfter = False
                        break
                if isAfter:
                    dp[j] = max(dp[j], dp[k] + 1)
        return len(A[0]) - max(dp)
