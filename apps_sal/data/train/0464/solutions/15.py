class Solution:
    def minOperations(self, n: int) -> int:
        mid=0
        count=0
        if n%2 == 0:
            mid = ((n//2)*2+1 + (n//2-1)*2 +1)//2
            for i in range(n//2):
                count=count + mid-(i*2+1) 
                
        else:
            mid = ((n-1)//2)*2 +1
            for i in range(n//2):
                count=count + mid-(i*2+1) 
                
                
        return count
