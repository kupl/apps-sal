class Solution:

    def stoneGameIII(self, stoneValue: List[int]) -> str:
        A = stoneValue
        dp = [0] * 3
        for i in range(len(A) - 1, -1, -1):
            dp[i % 3] = max((sum(A[i:i + k]) - dp[(i + k) % 3] for k in (1, 2, 3)))
        if dp[0] > 0:
            return 'Alice'
        elif dp[0] < 0:
            return 'Bob'
        else:
            return 'Tie'
