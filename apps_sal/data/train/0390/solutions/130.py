class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        squares = [i * i for i in range(1, int(n ** 0.5) + 1)]
        
        DP = [0] * (1 + n)
        for i in range(1, n + 1):
            can_win = False
            for s in squares:
                if s > i:
                    break
                can_win |= not DP[i - s]
            DP[i] = can_win
        return DP[-1]
