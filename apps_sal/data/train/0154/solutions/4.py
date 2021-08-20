class Solution:

    def maxArea(self, h: int, w: int, hc: List[int], v: List[int]) -> int:
        hc.append(0)
        hc.append(h)
        v.append(0)
        v.append(w)
        v.sort()
        hc.sort()
        max_v = max_h = 0
        for i in range(1, len(hc)):
            max_h = max(max_h, hc[i] - hc[i - 1])
        for i in range(1, len(v)):
            max_v = max(max_v, v[i] - v[i - 1])
        return max_h * max_v % 1000000007
