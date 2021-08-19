class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = [0] * (n + 1)
        squares = []
        i = 1
        nxt_sqrt = 1
        nxt = 1
        for i in range(1, n + 1):
            if i == nxt:
                dp[i] = 1
                squares.append(nxt)
                nxt_sqrt += 1
                nxt = nxt_sqrt ** 2
            else:
                dp[i] = max(-dp[i - s] for s in squares)
        return dp[n] == 1

#         squares = [i**2 for i in range(1, int(sqrt(n)) + 1)]

#         for s in squares:
#             dp[s] = 1

        # @lru_cache(None)
        # def play(n):
        #     sq = sqrt(n)
        #     if int(sq) == sq:
        #         return 1
        #     best = -1
        #     for i in range(int(sq), 0, -1):
        #         best = max(best, -play(n - i ** 2))
        #     return best
        # return play(n) == 1
