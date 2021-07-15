class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        
        alice = [False]*(n+1)
        bob = [False]*(n+1)
                
        for i in range(1, n+1):
            for x in range(1, int(sqrt(i))+1):
                if not bob[i-x*x]:
                    alice[i] = True
                    break
            for x in range(1, int(sqrt(i))+1):
                if not alice[i-x*x]:
                    bob[i] = True
                    break
            
        return alice[n]

