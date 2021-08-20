class Solution:

    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        mod = 10 ** 9 + 7
        horizontalCuts += [0, h]
        horizontalCuts.sort()
        verticalCuts += [0, w]
        verticalCuts.sort()
        hor_max = 0
        for i in range(len(horizontalCuts) - 1):
            hor_max = max(hor_max, abs(horizontalCuts[i] - horizontalCuts[i + 1]))
        ver_max = 0
        for i in range(len(verticalCuts) - 1):
            ver_max = max(ver_max, abs(verticalCuts[i] - verticalCuts[i + 1]))
        return hor_max * ver_max % mod
