class Solution:
    def minOperations(self, n: int) -> int:
        s = 0
        for i in range(n):
            s = s + 2*i+1
        x = s//n
        print(x)
        y = 0
        for i in range(n):
            if(2*i+1<x):
                y = y+x-(2*i+1)
        return y
            
            
        
        

