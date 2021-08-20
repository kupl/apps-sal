class Solution:

    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        verticalCuts.sort()
        prev = 0
        hDiff = 0
        for horiz in horizontalCuts:
            hDiff = max(hDiff, horiz - prev)
            prev = horiz
        hDiff = max(h - prev, hDiff)
        prev = 0
        vDiff = 0
        for vert in verticalCuts:
            vDiff = max(vDiff, vert - prev)
            prev = vert
        vDiff = max(w - prev, vDiff)
        return vDiff * hDiff % (10 ** 9 + 7)
