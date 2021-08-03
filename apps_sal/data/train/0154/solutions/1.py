class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        h_max = self.get_max_interval(w, sorted(verticalCuts))
        w_max = self.get_max_interval(h, sorted(horizontalCuts))
        return (h_max * w_max) % (10**9 + 7)

    def get_max_interval(self, length, cuts):
        current = 0
        max_cut = 0
        for cut in cuts:
            max_cut = max(max_cut, cut - current)
            current = cut

        max_cut = max(max_cut, length - current)
        return max_cut
