class Solution:
    def nthPersonGetsNthSeat(self, n: int) -> float:
        i = 0
        if n ==1:
            return 1
        
        notCorrect = 1/n
        
        for i in range(1,n-1):
            notCorrect*= (1.0 + 1.0/(n-i))
        
        
        return 1-notCorrect
