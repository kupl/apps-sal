class Solution:
    def minOperations(self, n: int) -> int:
        if n == 1:
            return 0
        result = 0
        for i in range(n//2):
            if n % 2 != 0:
                result += 2*(i+1)
            else:
                result += 1+ 2*i
        return result
    
        

