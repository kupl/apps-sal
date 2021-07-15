class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        res = [False] * (n+1)
        
        for i in range(1, n+1):
            j = 1
            while j * j <= i:
                res[i] |= not res[i-j*j]
                if res[i]: break
                j += 1
        return res[n]

