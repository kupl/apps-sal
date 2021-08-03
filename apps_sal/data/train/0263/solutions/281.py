class Solution:
    def knightDialer(self, n: int) -> int:
        possibleMoves = {0: [4, 6], 1: [6, 8], 2: [9, 7], 3: [4, 8], 4: [0, 3, 9], 5: [], 6: [0, 1, 7], 7: [2, 6], 8: [1, 3], 9: [2, 4]}
        upper = 10**9 + 7
        cache = {}

        def dfs(steps, loc):
            if (steps, loc) in cache:
                return cache[(steps, loc)]
            if steps == 0:
                return 1
            ans = 0
            for stop in possibleMoves[loc]:
                ans = (ans + dfs(steps - 1, stop)) % upper
            cache[(steps, loc)] = ans
            return ans
        return sum(dfs(n - 1, loc) for loc in possibleMoves) % upper
