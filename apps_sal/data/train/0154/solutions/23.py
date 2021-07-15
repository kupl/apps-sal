class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.append(0)
        horizontalCuts.append(h)
        
        verticalCuts.append(0)
        verticalCuts.append(w)
        
        horizontalCuts.sort()
        verticalCuts.sort()
        
        mw = 0
        mh = 0
        
        for x, y in zip(horizontalCuts, horizontalCuts[1:]):
            mw = max(mw, y-x)
        for x, y in zip(verticalCuts, verticalCuts[1:]):
            mh = max(mh, y-x)
        mod = 10**9 + 7
        return (mw * mh) % mod
