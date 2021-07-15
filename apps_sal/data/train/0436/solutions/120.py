memo={}; f=min
class Solution:
    def minDays(self, n: int) -> int:
        if n==0: 
            return 0
        if n==1:
            return 1
        if n in memo:
            return memo[n]
        
        
        sol = min(self.minDays(n//2)+n%2+1, self.minDays(n//3)+n%3+1)
        memo[n]=sol
        
        return sol
        



