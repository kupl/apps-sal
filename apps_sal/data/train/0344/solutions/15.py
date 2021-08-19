class Solution:

    def minDeletionSize(self, A: List[str]) -> int:
        l = len(A[0])
        dp = [1] * l
        for i in range(1, l):
            for j in range(i):
                if all((a[i] >= a[j] for a in A)):
                    dp[i] = max(dp[i], dp[j] + 1)
        return l - max(dp)
