class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        mod = int(1e9) + 7
        return (self.get_max_length(h, horizontalCuts) % mod) * (self.get_max_length(w, verticalCuts) % mod) % mod

    def get_max_length(self, length: int, cuts: List[int]) -> int:
        if len(cuts) == 1:
            return max(cuts[0], length - cuts[0])

        cuts.sort()
        max_length = max(cuts[0], length - cuts[-1])
        for i in range(1, len(cuts)):
            max_length = max(max_length, cuts[i] - cuts[i - 1])
        return max_length
