class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        mem={}
        def game(n):
            if n in mem:
                return mem[(n)]
            if n==0:
                return False
            k=1
            mem[n]=False
            while k*k<=n:
                if not game(n-k*k):
                    mem[n]=True
                    break
                k+=1
            return mem[n]
        
        game(n)
        return mem[n]

