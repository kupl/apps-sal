class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        
        memo = {}
        def helper(n):
            if n in memo:
                return memo[n]
            if n==0:
                return False
            if n==1:
                return True
            i=1
            while i*i<=n:
                win = helper(n-i*i)
                if not win:
                    memo[n] = True
                    return True 
                i+=1
            memo[n] = False
            return False
        res = helper(n)
        return res
    
        

