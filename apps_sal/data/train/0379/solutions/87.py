from collections import defaultdict
from functools import lru_cache


class Solution:

    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        mod = 10 ** 9 + 7
        mp = defaultdict(int)
        for (i, x) in enumerate(nums1):
            mp[0, x] = i
        for (i, x) in enumerate(nums2):
            mp[1, x] = i
        grid = [nums1, nums2]

        @lru_cache(None)
        def search(cur_row: int, i: int, prev_row: int) -> int:
            if cur_row == prev_row:
                res = grid[cur_row][i] + (search(cur_row, i + 1, cur_row) if i + 1 < len(grid[cur_row]) else 0)
                if (1 - cur_row, grid[cur_row][i]) in mp:
                    j = mp[1 - cur_row, grid[cur_row][i]]
                    res = max(res, search(1 - cur_row, j, cur_row))
                return res
            else:
                return grid[cur_row][i] + (search(cur_row, i + 1, cur_row) if i + 1 < len(grid[cur_row]) else 0)
        return max(search(0, 0, 0), search(1, 0, 1)) % mod
