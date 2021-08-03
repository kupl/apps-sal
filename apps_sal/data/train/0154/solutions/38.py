class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        verticalCuts.sort()
        max_h = horizontalCuts[0]
        for h_cut in range(1, len(horizontalCuts)):
            max_h = max(max_h, horizontalCuts[h_cut] - horizontalCuts[h_cut - 1])
        max_h = max(max_h, h - horizontalCuts[-1])
        max_v = verticalCuts[0]
        for v_cut in range(1, len(verticalCuts)):
            max_v = max(max_v, verticalCuts[v_cut] - verticalCuts[v_cut - 1])
        max_v = max(max_v, w - verticalCuts[-1])
        return max_h * max_v % int(1e9 + 7)
