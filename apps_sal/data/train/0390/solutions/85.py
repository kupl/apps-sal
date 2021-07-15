def canWin(n,squares,memo):
    
    if n in squares:
        #print(n,True)
        return True
    
    if n in memo:
        return memo[n]
    
    res = False
    for i in reversed(squares):
        if i>n: continue
        #if n==13: print('here',n-i)
        if not canWin(n-i,squares,memo):
            res = True
            break
            
    memo[n] = res
    return res
    

class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        squares = [i**2 for i in range(1,floor(sqrt(n))+1)]
        memo = dict()
        print(squares)
        return canWin(n,squares,memo)
        

