class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        ver = [0] + sorted(verticalCuts) + [w]
        hor = [0] + sorted(horizontalCuts) + [h]

        dh = max(hor[i] - hor[i - 1] for i in range(1, len(hor)))
        dv = max(ver[i] - ver[i - 1] for i in range(1, len(ver)))

        return dh * dv % (10**9 + 7)
