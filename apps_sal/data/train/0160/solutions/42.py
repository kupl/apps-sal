class Solution:

    def stoneGame(self, piles: List[int]) -> bool:
        memo = {}

        def dfs(i, j, alex):
            if (i, j, alex) in memo:
                return memo[i, j, alex]
            if i >= j:
                return 0
            left = dfs(i + 1, j, not alex)
            right = dfs(i, j - 1, not alex)
            if not alex:
                ans = min(left, right)
            else:
                ans = max(left + piles[i], right + piles[j])
            memo[i, j, alex] = ans
            return ans
        a = dfs(0, len(piles) - 1, True)
        return a > sum(piles) / 2
