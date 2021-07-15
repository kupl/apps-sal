class Solution:
    def knightDialer(self, n: int) -> int:
        if n == 1:
            return 10
        
        mod = 10**9+7
        dc = {
              (0,1): 1,
              (1,1): 1,
              (2,1): 1,
              (3,1): 1,
              (4,1): 1,
              (5,1): 1,
              (6,1): 1,
              (7,1): 1,
              (8,1): 1,
              (9,1): 1,
             }
        
        for i in range(n-1):
            dc[(0,i+2)] = (dc[(4,i+1)] + dc[(6,i+1)]) % mod 
            dc[(1,i+2)] = (dc[(6,i+1)] + dc[(8,i+1)]) % mod
            dc[(2,i+2)] = (dc[(7,i+1)] + dc[(9,i+1)]) % mod 
            dc[(3,i+2)] = (dc[(4,i+1)] + dc[(8,i+1)]) % mod 
            dc[(4,i+2)] = (dc[(0,i+1)] + dc[(3,i+1)] + dc[(9,i+1)]) % mod 
            dc[(5,i+2)] = 0 
            dc[(6,i+2)] = (dc[(0,i+1)] + dc[(1,i+1)] + dc[(7,i+1)]) % mod
            dc[(7,i+2)] = (dc[(2,i+1)] + dc[(6,i+1)]) % mod
            dc[(8,i+2)] = (dc[(1,i+1)] + dc[(3,i+1)]) % mod 
            dc[(9,i+2)] = (dc[(2,i+1)] + dc[(4,i+1)]) % mod
            
        res = 0
        for j in range(10):
            res = (res + dc[(j,n)]) % mod
        return res
