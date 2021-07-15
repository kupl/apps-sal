class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        
        M = {}
        M[0] = False
        M[1] = True
        for i in range(2, n+1):
            M[i] = False
            sq = int(math.sqrt(i))
            if sq**2 == i:
                M[i] = True
            for j in range(1, sq + 1):
                M[i] = M[i] or not M[i-(j*j)]
        return M[n]
            
        

