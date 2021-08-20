class Solution:

    def maxArea(self, h: int, w: int, hCuts: List[int], vCuts: List[int]) -> int:
        hCuts.sort()
        vCuts.sort()
        (H, V) = (max(hCuts[0], h - hCuts[-1]), max(vCuts[0], w - vCuts[-1]))
        for i in range(1, len(hCuts)):
            H = max(H, hCuts[i] - hCuts[i - 1])
        for i in range(1, len(vCuts)):
            V = max(V, vCuts[i] - vCuts[i - 1])
        return H * V % 1000000007
