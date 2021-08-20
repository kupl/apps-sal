class Solution:

    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:

        def getMaxSpace(cuts, upperLimit):
            cuts.sort()
            if not any(cuts):
                return upperLimit
            ans = cuts[0]
            for i in range(len(cuts) - 1):
                ans = max(ans, cuts[i + 1] - cuts[i])
            return max(ans, upperLimit - cuts[-1])
        maxHorSpace = getMaxSpace(horizontalCuts, h)
        maxVertSpace = getMaxSpace(verticalCuts, w)
        mod = 1000000000.0 + 7
        return int(maxHorSpace * maxVertSpace % mod)
