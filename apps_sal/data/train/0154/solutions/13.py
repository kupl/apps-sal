class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        mod = 10**9 + 7
        horizontalCuts.extend([0, h])
        horizontalCuts.sort()
        verticalCuts.extend([0, w])
        verticalCuts.sort()
        hor_max = 0
        for i in range(len(horizontalCuts)-1):
            hor_max = max(hor_max, horizontalCuts[i+1] - horizontalCuts[i])
        
        ver_max = 0
        for i in range(len(verticalCuts)-1):
            ver_max = max(ver_max, verticalCuts[i+1] - verticalCuts[i])
        return (hor_max*ver_max)%mod
       
                

