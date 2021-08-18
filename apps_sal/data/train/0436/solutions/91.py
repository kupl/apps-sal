class Solution:
    def minDays(self, n: int) -> int:

        def dfs(numOrngs):

            if numOrngs in seen:
                return seen[numOrngs]

            if numOrngs == 0:
                return 0

            if numOrngs < 0:
                return float('inf')

            seen[numOrngs] = min((numOrngs % 2) + dfs(numOrngs // 2), (numOrngs % 3) + dfs(numOrngs // 3)) + 1

            return seen[numOrngs]

        seen = {}
        return dfs(n) - 1
