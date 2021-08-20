class Solution:

    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        verticalCuts.sort()
        max_width = verticalCuts[0]
        max_height = horizontalCuts[0]
        for i in range(len(horizontalCuts) - 1):
            max_height = max(max_height, horizontalCuts[i + 1] - horizontalCuts[i])
        max_height = max(max_height, h - horizontalCuts[-1])
        for i in range(len(verticalCuts) - 1):
            max_width = max(max_width, verticalCuts[i + 1] - verticalCuts[i])
        max_width = max(max_width, w - verticalCuts[-1])
        return max_height * max_width % (10 ** 9 + 7)
