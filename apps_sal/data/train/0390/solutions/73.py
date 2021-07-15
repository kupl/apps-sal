class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        res = [False] * (n+1)
        for i in range(n+1):
            if res[i]: continue
            j = 1
            while i + j * j <= n:
                res[i + j*j] = True
                j += 1
        return res[n]

