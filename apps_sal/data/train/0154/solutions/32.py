class Solution:

    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        verticalCuts.sort()
        max_h = max(horizontalCuts[0], h - horizontalCuts[-1])
        if len(horizontalCuts) > 1:
            for i in range(len(horizontalCuts) - 1):
                if max_h < abs(horizontalCuts[i + 1] - horizontalCuts[i]):
                    max_h = abs(horizontalCuts[i + 1] - horizontalCuts[i])
        max_v = max(verticalCuts[0], w - verticalCuts[-1])
        if len(verticalCuts) > 1:
            for i in range(len(verticalCuts) - 1):
                if max_v < abs(verticalCuts[i + 1] - verticalCuts[i]):
                    max_v = abs(verticalCuts[i + 1] - verticalCuts[i])
        return max_h % (10 ** 9 + 7) * (max_v % (10 ** 9 + 7)) % (10 ** 9 + 7)
