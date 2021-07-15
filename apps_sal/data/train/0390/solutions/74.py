class Solution:
    #   1(T)   2(F)   3(T)   4(T)   5   6   7
    def winnerSquareGame(self, n: int) -> bool:
        mem = {}
        if int(pow(n,0.5)) == pow(n,0.5):
            return True
        def helper(n):
            if n in mem:
                return mem[n]
            for i in range(1,int(pow(n,0.5))+1):
                if not helper(n-i*i):  # try that move and won
                    mem[n] = True
                    return True
            mem[n] = False
            return False
        return helper(n)
