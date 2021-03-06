import collections
import functools
import heapq
import itertools
import sys
from functools import lru_cache
from typing import List
'\n每个人都不同喜欢的帽子，求分配方案数量\n\nhats = [[3,4],[4,5],[5]]\n1\n\ndfs: \n\t   [3,4]\n\t     | \n\t   [4,5]\n\n显然：\n\tdp[start_person + 1][chose_hats + new_in] += dp[start_person][chose_hats + new_in]\n\t   \nn == hats.length\n1 <= n <= 10\n1 <= hats[i].length <= 40\n\n\n'


class Solution:

    def numberWays(self, hats: List[List[int]]) -> int:
        LIMIT = 10 ** 9 + 7
        n = len(hats)
        final = 0
        dp = collections.defaultdict(lambda: -1)

        def dfs(row, path):
            if row >= n:
                return 0
            count = 0
            for hat in hats[row]:
                if 1 << hat & path:
                    continue
                if row == n - 1:
                    count += 1
                count += dfs(row + 1, path | 1 << hat)
            return count % LIMIT

        def dfs_dp(row, path):
            if row >= n:
                return 0
            if dp[row, path] != -1:
                return dp[row, path]
            count = 0
            for hat in hats[row]:
                if 1 << hat & path:
                    continue
                if row == n - 1:
                    count += 1
                count += dfs_dp(row + 1, path | 1 << hat)
            dp[row, path] = count % LIMIT
            return count % LIMIT
        hat_map = collections.defaultdict(set)
        for (person, j) in enumerate(hats):
            for hat in j:
                hat_map[hat].add(person)
        hats_list = list(hat_map.keys())
        hats_n = len(hats_list)
        final = pow(2, n) - 1

        def dfs_dp1(hat_index, path):
            if hat_index >= hats_n:
                if path == final:
                    return 1
                return 0
            if dp[hat_index, path] != -1:
                return dp[hat_index, path]
            count = 0
            for person in hat_map[hats_list[hat_index]]:
                if 1 << person & path:
                    continue
                count += dfs_dp1(hat_index + 1, path | 1 << person)
            count += dfs_dp1(hat_index + 1, path)
            dp[hat_index, path] = count % LIMIT
            return count % LIMIT
        return dfs_dp1(0, 0)
