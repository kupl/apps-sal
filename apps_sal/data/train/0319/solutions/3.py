class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)

        A = stoneValue
        dp = [0] * 3
        for i in range(n - 1, -1, -1):
            dp[i % 3] = max(sum(A[i:i + k]) - dp[(i + k) % 3] for k in (1, 2, 3))
        c = dp[0]
        if c > 0:
            return 'Alice'
        elif c == 0:
            return 'Tie'
        else:
            return 'Bob'
