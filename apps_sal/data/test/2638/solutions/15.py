class Solution:
    def minimumTotal(self, triangle):
        self._min_cache = {}
        for i in reversed(list(range(len(triangle)))):
            for j in reversed(list(range(len(triangle[i])))):
                self.get_minimum_sum(triangle, i, j)
        return self.get_minimum_sum(triangle, 0, 0)

    def get_minimum_sum(self, triangle, level_i, item_j):
        if ((level_i, item_j) in self._min_cache):
            return self._min_cache[(level_i, item_j)]
        if level_i < 0 or level_i >= len(triangle):
            return 0
        level = triangle[level_i]

        if item_j < 0 or item_j > len(level):
            return 0

        item = level[item_j]

        min_v = item + min(self.get_minimum_sum(triangle, level_i + 1, item_j),
                           self.get_minimum_sum(triangle, level_i + 1, item_j + 1))
        self._min_cache[(level_i, item_j)] = min_v

        return min_v
