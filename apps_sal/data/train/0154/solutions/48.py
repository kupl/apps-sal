class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts, verticalCuts = sorted([0, h]+horizontalCuts), sorted([0, w]+verticalCuts)
        return max([after-prev for after, prev in zip(horizontalCuts[1:], horizontalCuts)])*max([after-prev for after, prev in zip(verticalCuts[1:], verticalCuts)])%(10**9+7)
