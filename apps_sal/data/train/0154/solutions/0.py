class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        mod = int(1e9)+7
        return ( ( self.getMax(horizontalCuts, h) % mod ) * ( self.getMax(verticalCuts, w) % mod ) ) % mod
        
    def getMax(self, cuts, size):
        if len(cuts) == 1:
            return max(cuts[0], size - cuts[0])
        
        cuts.sort()
        
        max_cut_size = max(cuts[0], size - cuts[-1])
        for index in range(1, len(cuts)):
            if cuts[index] - cuts[index - 1] > max_cut_size:
                max_cut_size = cuts[index] - cuts[index - 1]
        
        return max_cut_size
