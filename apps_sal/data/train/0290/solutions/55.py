import itertools
import sys
from functools import lru_cache
from math import comb
from typing import List
'\n给你一个整数数组 cuts ，其中 cuts[i] 表示你需要将棍子切开的位置。定义切割成本是要切割的棍子长度，求最小的切割成本，即找到一个最小成本的切割顺序\n\n\nn = 7, cuts = [1,3,4,5]\n0 1| 2 3| 4| 5| 6 7\n\ndfs:\n        a\n      b c d\n      \ndp[start][end]= min(dp[start][cut] + dp[cut][end])\n斜向上扫描。\n\n\n'


class Solution1:

    def dfs(self, start, end, path, cuts):
        if self.dp[start][end] != sys.maxsize:
            return self.dp[start][end]
        min_cut = sys.maxsize
        flag = False
        nums = cuts[self.cuts_map[start]:self.cuts_map[end]]
        for cut in nums:
            if cut not in path and start < cut and (cut < end):
                flag = True
                path.add(cut)
                min_cut = min(min_cut, end - start + self.dfs(start, cut, path, cuts) + self.dfs(cut, end, path, cuts))
                path.remove(cut)
        if not flag:
            min_cut = 0
        self.dp[start][end] = min_cut
        return min_cut

    def minCost(self, n: int, cuts: List[int]) -> int:
        self.dp = [[sys.maxsize for _ in range(n + 1)] for _ in range(n + 1)]
        cuts = sorted(cuts)
        self.cuts_map = {}
        for (i, cut) in enumerate(cuts):
            self.cuts_map[cut] = i
        self.cuts_map[0] = 0
        self.cuts_map[n] = n
        return self.dfs(0, n, set(), cuts)


class Solution:

    def dfs(self, start, end, path, cuts):
        if self.dp[self.cuts_map[start]][self.cuts_map[end]] != sys.maxsize:
            return self.dp[self.cuts_map[start]][self.cuts_map[end]]
        min_cut = sys.maxsize
        flag = False
        nums = cuts[self.cuts_map[start]:self.cuts_map[end]]
        for cut in nums:
            if cut not in path and start < cut and (cut < end):
                flag = True
                path.add(cut)
                min_cut = min(min_cut, end - start + self.dfs(start, cut, path, cuts) + self.dfs(cut, end, path, cuts))
                path.remove(cut)
        if not flag:
            min_cut = 0
        self.dp[self.cuts_map[start]][self.cuts_map[end]] = min_cut
        return min_cut

    def minCost(self, n: int, cuts: List[int]) -> int:
        self.dp = [[sys.maxsize for _ in range(len(cuts) + 2)] for _ in range(len(cuts) + 2)]
        cuts.extend([0, n])
        cuts = sorted(cuts)
        self.cuts_map = {}
        for (i, cut) in enumerate(cuts):
            self.cuts_map[cut] = i
        return self.dfs(0, n, set(), cuts)
