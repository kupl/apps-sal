class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        verticalCuts.sort()
        print(horizontalCuts, verticalCuts)
        pre = 0
        hori_max = 0
        for i, cut in enumerate(horizontalCuts):
            hori_max = max(hori_max, cut - pre)
            pre = cut

        hori_max = max(hori_max, h - pre)
        pre = 0
        vert_max = 0
        for i, cut in enumerate(verticalCuts):
            vert_max = max(vert_max, cut - pre)
            pre = cut

        vert_max = max(vert_max, w - pre)
        return (hori_max * vert_max) % (10**9 + 7)
