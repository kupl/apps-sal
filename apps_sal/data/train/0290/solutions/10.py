class Solution:

    def minCost(self, n: int, cuts: List[int]) -> int:

        @lru_cache(None)
        def solve(l, r):
            best = n * n
            found = False
            for c in cuts:
                if c <= l or c >= r:
                    continue
                found = True
                best = min(best, r - l + solve(l, c) + solve(c, r))
            if not found:
                return 0
            return best
        return solve(0, n)
