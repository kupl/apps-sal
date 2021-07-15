class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        #squares = [i * i for i in range(1, int(n ** 0.5) + 1)]
        
        DP = [0] * (1 + n)
        for i in range(1, n + 1):
            DP[i] = not all(DP[i - j * j] for j in range(1, int(i ** 0.5) + 1))
        return DP[-1]
