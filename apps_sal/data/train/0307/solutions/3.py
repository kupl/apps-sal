class Solution:
    def soupServings(self, N: int) -> float:
        def f(a,b):
            if a <= 0 and b <= 0:
                return 0.5
            if a <= 0:
                return 1
            if b <= 0:
                return 0
            if _memo[a][b] >0:
                return _memo[a][b]
            
            _memo[a][b] = 0.25 *(f(a - 4,b) + f(a - 3,b - 1)  + f(a - 2,b - 2)  + f(a - 1,b - 3) ) 
            return _memo[a][b]
        _memo = [[0] * 200 for i in range(200)]
        
        if N >= 4800:
            return 1
        else:
            return f((N + 24) // 25, (N + 24) // 25)
         
            
            

