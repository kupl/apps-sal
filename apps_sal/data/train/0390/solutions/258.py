class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = [False] * (n + 1)  # true is on peut gagner le jeu avec i pierre
        for i in range(1, n + 1):
            dp[i] = not all(dp[i - k * k] for k in range(1, int(i**0.5) + 1))  # si tout gagne après notre coup (quel qu'il soit), on perd
        return dp[-1]
