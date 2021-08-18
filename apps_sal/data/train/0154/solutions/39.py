class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        verticalCuts.sort()
        max_hor_width = horizontalCuts[0]
        for i in range(len(horizontalCuts) - 1):
            max_hor_width = max(max_hor_width, horizontalCuts[i + 1] - horizontalCuts[i])
        max_hor_width = max(max_hor_width, h - horizontalCuts[len(horizontalCuts) - 1])

        max_vert_width = verticalCuts[0]
        for i in range(len(verticalCuts) - 1):
            max_vert_width = max(max_vert_width, verticalCuts[i + 1] - verticalCuts[i])
        max_vert_width = max(max_vert_width, w - verticalCuts[len(verticalCuts) - 1])

        return (max_vert_width * max_hor_width) % 1000000007
