class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        verticalCuts.sort()
        hr = [0] + horizontalCuts + [h]
        vr = [0] + verticalCuts + [w]
        hmax, vmax = 0, 0
        for i in range(1, len(hr)):
            hmax = max(hmax, hr[i] - hr[i - 1])
        for i in range(1, len(vr)):
            vmax = max(vmax, vr[i] - vr[i - 1])
        return (hmax * vmax) % (10**9 + 7)
