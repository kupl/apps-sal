class Solution:

    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        verticalCuts.sort()
        mx = max(verticalCuts[0], w - verticalCuts[-1])
        my = max(horizontalCuts[0], h - horizontalCuts[-1])
        for i in range(1, len(verticalCuts)):
            mx = max(mx, verticalCuts[i] - verticalCuts[i - 1])
        for i in range(1, len(horizontalCuts)):
            my = max(my, horizontalCuts[i] - horizontalCuts[i - 1])
        return mx * my % (10 ** 9 + 7)
