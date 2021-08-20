class Solution:

    def winnerSquareGame(self, n: int) -> bool:
        mem = {}
        squares = []
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

    def calcSquares(self, mem, squares, n):
        for i in range(1, n):
            i = pow(i, 0.5)
            if int(i) == i:
                squares.append(i)
                mem[i] = True
