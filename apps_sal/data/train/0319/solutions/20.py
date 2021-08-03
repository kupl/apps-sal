class Solution:
    def stoneGameIII(self, S: List[int]) -> str:

        n = len(S)

        dp = [0] * n

        for i in range(n)[::-1]:
            M = float('-inf')
            for k in range(1, 4):
                M = max(M, sum(S[i:i + k]) - (dp[i + k] if i + k < n else 0))
            dp[i] = M

        if dp[0] > 0:
            return 'Alice'
        elif dp[0] < 0:
            return 'Bob'
        else:
            return 'Tie'
