class Solution:

    def getMax(self, max: int, cuts: List[int]) -> int:
        last = 0
        for x in cuts:
            cur = x - last
            if cur > max:
                max = cur
            last = x
        return max

    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        mod = 1000000007
        horizontalCuts.sort()
        verticalCuts.sort()
        maxh = self.getMax(h - horizontalCuts[-1], horizontalCuts)
        maxv = self.getMax(w - verticalCuts[-1], verticalCuts)
        return maxh % mod * maxv % mod
