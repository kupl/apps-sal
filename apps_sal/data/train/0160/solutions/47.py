class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        if not piles:
            return False

        cache = {}

        def dfs(l, r):
            # Calculate the best sum of Alex.
            if l >= r + 1:
                return 0
            if (l, r) in cache:
                return cache[(l, r)]
            res = max(piles[l] + min(dfs(l + 2, r), dfs(l + 1, r - 1)), piles[r] + min(dfs(l, r - 2), dfs(l + 1, r - 1)))
            cache[(l, r)] = res
            return cache[(l, r)]

        sum_a = dfs(0, len(piles) - 1)
        sum_b = sum(piles) - sum_a
        # print(sum_a)
        return sum_a > sum_b
