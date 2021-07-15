class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.append(0)
        horizontalCuts.append(h)
        horizontalCuts.sort()
        Maxh = max([horizontalCuts[i] - horizontalCuts[i-1] for i in range(1,len(horizontalCuts))])
        verticalCuts.append(0)
        verticalCuts.append(w)
        verticalCuts.sort()
        Maxv = max([verticalCuts[i] - verticalCuts[i-1] for i in range(1,len(verticalCuts))])
        
        return Maxh*Maxv % 1000000007
