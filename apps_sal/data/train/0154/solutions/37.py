class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        modu = 1000000007
        
        # horizontal- i
        # vertical-j
        # 横向记录0-x, x-y, y-m留下最大
        # 竖向也一样
        
        h_max = 0
        v_max = 0
        
        horizontalCuts.append(0)
        horizontalCuts.append(h)
        
        verticalCuts.append(0)
        verticalCuts.append(w)
        
        horizontalCuts.sort()
        verticalCuts.sort()
        
        for i in range(1,len(horizontalCuts)):
            h_max = max(h_max, horizontalCuts[i]-horizontalCuts[i-1])
        
        for j in range(1,len(verticalCuts)):
            v_max = max(v_max, verticalCuts[j]-verticalCuts[j-1])
        
        return (v_max*h_max)%modu
