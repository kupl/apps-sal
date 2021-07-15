class Solution:
    def soupServings(self, N: int) -> float:
        operations = [(100, 0), (75, 25), (50, 50), (25, 75)]
        @lru_cache(maxsize=None)
        def helper(remainA, remainB):
            if remainA == 0 and remainB == 0:
                return 0.5

            if remainA == 0 or remainB == 0:
                return remainA == 0

            result = 0
            for op in operations:
                result += helper(max(0, remainA - op[0]), max(0, remainB - op[1]))

            return result / 4
        
        N = min(N, 4801)
        return helper(N, N)
