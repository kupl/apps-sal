class Solution:

    def stoneGameIII(self, A: List[int]) -> str:
        n = len(A)
        dp = [-float('inf')] * n
        A.reverse()
        for (i, x) in enumerate(A):
            adding = 0
            for j in range(3):
                if i - j >= 0:
                    adding += A[i - j]
                    dp[i] = max(dp[i], adding - (dp[i - j - 1] if i - j >= 1 else 0))
        if dp[-1] < 0:
            return 'Bob'
        return 'Tie' if dp[-1] == 0 else 'Alice'
