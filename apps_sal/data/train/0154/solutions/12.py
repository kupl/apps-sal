class Solution:
    def maxArea(self, h: int, w: int, hc: List[int], vc: List[int]) -> int:
        hc, vc = [0] + sorted(hc) + [h], [0] + sorted(vc) + [w]
        return max(hc[i] - hc[i-1] for i in range(1, len(hc))) * max(vc[i] - vc[i-1] for i in range(1, len(vc))) % 1000000007
