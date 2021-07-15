class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        opt = [False] * (n+1)
        for i in range(1, n+1):
            for j in range(1, int(i**0.5)+1):
                if not opt[i - j*j]:
                    opt[i] = True
                    break
        return opt[n]
                    
        

