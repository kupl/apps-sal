class Solution:

    def winnerSquareGame(self, n: int) -> bool:
        mem = [None] * (n + 1)

        def dp(k):
            if k == 0:
                return -1
            if mem[k] != None:
                return mem[k]
            for i in range(int(math.sqrt(k)), 0, -1):
                if dp(k - i * i) < 0:
                    mem[k] = 1
                    return 1
            mem[k] = -1
            return -1
        return dp(n) > 0
