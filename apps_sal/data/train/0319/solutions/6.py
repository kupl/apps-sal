class Solution:

    def stoneGameIII(self, S: List[int]) -> str:
        n = len(S)
        dp = [0] * n
        for i in range(n)[::-1]:
            dp[i] = max((sum(S[i:i + k]) - (dp[i + k] if i + k < n else 0) for k in (1, 2, 3)))
        if dp[0] > 0:
            return 'Alice'
        elif dp[0] < 0:
            return 'Bob'
        else:
            return 'Tie'
