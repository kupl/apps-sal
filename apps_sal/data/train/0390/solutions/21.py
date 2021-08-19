class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        mem = [None] * (n + 1)

        def dp(k):  # 有k个石头时，能否赢
            if k == 0:
                return -1
            if mem[k] != None:
                return mem[k]
            for i in range(int(math.sqrt(k)), 0, -1):
                if dp(k - i * i) < 0:  # 如果我取i*i个石头，剩下k-i*i个石头时，我最后没石头取输了，则代表有k
                    # 个石头胜利了，我可以取i*i个石头
                    mem[k] = 1
                    return 1
            mem[k] = -1
            return -1
        return dp(n) > 0
