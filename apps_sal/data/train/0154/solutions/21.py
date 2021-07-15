class Solution:
    
    
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        # Return ans % (1E9 + 7)
        # A = ((vi+1) - vi)*(hi+1 - hi)
        
        def getMaxSpace(cuts, upperLimit):
            cuts = sorted(cuts)
            if not any(cuts):
                return upperLimit
            
            ans = cuts[0] # first piece is 0 to first cut
            for i in range(len(cuts)-1):
                ans = max(ans, cuts[i+1] - cuts[i])
            return max(ans, upperLimit - cuts[-1])
        
        maxHorSpace = getMaxSpace(horizontalCuts, h)
        maxVertSpace = getMaxSpace(verticalCuts, w)
        
        mod = 1E9+7
        return int((maxHorSpace * maxVertSpace) % mod)

