class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        # Square numbers: 1, 4, 9, 16, 25...

        def removeSquare(n: int, memo: [int]):
            
            if n == 0: return False
            if memo[n]: return memo[n]

            i = 1
            
            while i*i <= n:
                
                if memo[n-(i*i)] == False: return True
                
                memo[n-(i*i)] = removeSquare(n-(i*i), memo)
                
                # If you can make a move, that will result
                # in the case: n==0
                # Then you can win
                if memo[n-(i*i)] == False:
                    return True
                
                i += 1
                
            return False
        
        memo = [None] * (n+1)
        
        return removeSquare(n, memo)
