class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        res = [0] * (n + 1)
        res[1] = 1
        for i in range(2, n + 1):
            for j in range(1, int(math.sqrt(i)) + 1):
                if not res[i-j*j]:
                    res[i] = 1
                    break
        print(res)
        return res[-1]
