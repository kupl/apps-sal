class Solution:
    def stoneGameIII(self, A: List[int]) -> str:
        dp = [0] * 3
        for i in range(len(A) - 1, -1, -1):
            dp[i % 3] = max(sum(A[i:i + k]) - dp[(i + k) % 3] for k in range(1, 4))
        if dp[0] > 0:
            return 'Alice'
        if dp[0] < 0:
            return 'Bob'
        return 'Tie'
