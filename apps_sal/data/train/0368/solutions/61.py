class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        totalDishes = len(satisfaction)
        
        dp = {}
        
        def cookOne(i0, n0):
            if i0 == totalDishes:
                return 0
            if (i0, n0) in dp:
                return dp[(i0, n0)]
            if satisfaction[i0] >= 0:
                dp[(i0, n0)] = (n0+1)*satisfaction[i0] + cookOne(i0+1, n0+1)
            else:
                dp[(i0, n0)] = max((n0+1)*satisfaction[i0] + cookOne(i0+1, n0+1), cookOne(i0+1, n0))
            
            return dp[(i0, n0)]
        
        return cookOne(0, 0)

