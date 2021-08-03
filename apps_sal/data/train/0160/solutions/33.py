class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        presum = [0]
        for pile in piles:
            presum.append(presum[-1] + pile)

        @lru_cache(None)
        def solve(a, b):
            if a == b:
                return piles[a]
            return max(presum[b + 1] - presum[a] - solve(a + 1, b), presum[b + 1] - presum[a] - solve(a, b - 1))
        gain = solve(0, len(piles) - 1)
        return gain > presum[-1] - gain
