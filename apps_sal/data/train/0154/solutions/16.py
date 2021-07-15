class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        def get_max_length(length: int, cuts: List[int]) -> int:
            if len(cuts) == 1:
                return max(cuts[0], length - cuts[0])

            cuts.sort()
            max_length = max(cuts[0], length - cuts[-1])
            for i in range(1, len(cuts)):
                # max_length = max(max_length, cuts[i] - cuts[i - 1])
                if cuts[i] - cuts[i - 1] > max_length:
                    max_length = cuts[i] - cuts[i - 1]
            return max_length

        return get_max_length(h, horizontalCuts) * get_max_length(w, verticalCuts) % 1000000007
