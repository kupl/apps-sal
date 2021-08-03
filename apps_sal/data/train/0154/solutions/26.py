class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        verticalCuts.sort()
        max_h, max_w = max(horizontalCuts[0], h - horizontalCuts[-1]), max(verticalCuts[0], w - verticalCuts[-1])
        for i in range(1, len(horizontalCuts)):
            max_h = max(max_h, horizontalCuts[i] - horizontalCuts[i - 1])
        for j in range(1, len(verticalCuts)):
            max_w = max(max_w, verticalCuts[j] - verticalCuts[j - 1])
        return (max_w * max_h) % (10**9 + 7)
