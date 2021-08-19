from collections import defaultdict


class Solution:

    def lenLongestFibSubseq(self, ordered_nums: List[int]) -> int:

        def dfs(prev, curr):
            if (prev, curr) in explored:
                return -1
            elif prev + curr not in unordered_nums:
                return 2
            else:
                explored.add((prev, curr))
                return 1 + dfs(curr, prev + curr)
        unordered_nums = {n for n in ordered_nums}
        explored = set()
        path_len = 0
        for i in range(len(unordered_nums)):
            for j in range(i + 1, len(unordered_nums)):
                path_len = max(path_len, dfs(ordered_nums[i], ordered_nums[j]))
        return path_len if path_len >= 3 else 0
