class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        mem = {}
        if int(pow(n, 0.5)) == pow(n, 0.5):
            return True

        def helper(n):
            if n in mem:
                return mem[n]
            for i in range(1, int(pow(n, 0.5)) + 1):
                if not helper(n - i * i):
                    mem[n] = True
                    return True
            mem[n] = False
            return False
        return helper(n)
