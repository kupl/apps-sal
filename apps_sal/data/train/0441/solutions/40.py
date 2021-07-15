class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        
        ini = 2
        re = 0
        
        while True:
            
            m = (N/ini) - (ini-1)/2
            
            if m <= 0:
                break
            
            elif m%1 == 0:
                re += 1
            
            ini += 1
        
        return re+1

