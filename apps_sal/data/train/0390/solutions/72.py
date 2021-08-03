class Solution:
    #   1(T)   2(F)   3(T)   4(T)   5   6   7
    def winnerSquareGame(self, n: int) -> bool:
        mem = {}
        squares = []
        if int(pow(n, 0.5)) == pow(n, 0.5):
            return True

        def helper(n):
            if n in mem:
                return mem[n]
            for i in range(1, int(pow(n, 0.5)) + 1):
                if not helper(n - i * i):  # try that move and won
                    mem[n] = True
                    return True
            mem[n] = False
            return False
        return helper(n)

    def calcSquares(self, mem, squares, n):
        for i in range(1, n):
            i = pow(i, 0.5)
            if int(i) == i:
                squares.append(i)
                mem[i] = True
