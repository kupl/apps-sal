fmax = lambda x,y: x if x>y else y
class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        
        i = n - 1
        
        i1, i2, i3 = 0, 0, 0
        
        while i>=0:
            ans = float('-inf')
            
            ans = fmax(ans, stoneValue[i] - i1)
            
            if i+1 < n:
                ans = fmax(ans, stoneValue[i] + stoneValue[i+1] - i2)
                
            if i+2 < n:
                ans = fmax(ans, stoneValue[i] + stoneValue[i+1] + stoneValue[i+2] - i3)
                
            i3 = i2
            i2 = i1
            i1 = ans
            i -= 1
        
        if i1 > 0:
            return 'Alice'
        elif i1 < 0:
            return 'Bob'
        return 'Tie'
