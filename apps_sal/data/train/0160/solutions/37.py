class Solution:

    def stoneGame(self, piles: List[int]) -> bool:
        total = sum(piles)
        pre_sums = [0] * (len(piles) + 1)
        for i in range(len(piles)):
            pre_sums[i + 1] = piles[i] + pre_sums[i]
        m = {}

        def dfs(start, end):
            if end == start:
                return piles[end]
            if (start, end) in m:
                return m[start, end]
            interval_total = pre_sums[end + 1] - pre_sums[start]
            max_stone = interval_total - min(dfs(start + 1, end), dfs(start, end - 1))
            m[start, end] = max_stone
            return max_stone
        Alex_score = dfs(0, len(piles) - 1)
        if Alex_score > total // 2:
            return True
        else:
            return False
