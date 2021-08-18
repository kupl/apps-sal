from collections import defaultdict


class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        if m == 0:
            return 0
        if not arr:
            return -1
        step = 0
        uf = UF(len(arr), m)
        res = -1
        for num in arr:
            step += 1
            if uf.add(num):
                res = step - 1

        if uf.cnt.get(m):
            return step
        return res


class UF:
    def __init__(self, n, m):
        self.max_length = n + 1
        self.target = m
        self.length_list = [0 for _ in range(self.max_length)]
        self.cnt = defaultdict(int)
        self.par = defaultdict(int)

    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        par_x = self.find(x)
        par_y = self.find(y)
        if par_x != par_y:
            self.par[par_x] = par_y
        self.cnt[self.length_list[par_x]] -= 1
        self.cnt[self.length_list[par_y]] -= 1
        self.length_list[par_y] += self.length_list[par_x]
        self.cnt[self.length_list[par_y]] += 1
        return False

    def add(self, x):
        tmp = self.cnt.get(self.target)
        self.par[x] = x
        self.length_list[x] = 1
        self.cnt[1] += 1
        if x >= 2 and self.length_list[x - 1] > 0:
            self.union(x, x - 1)
        if x <= self.max_length - 2 and self.length_list[x + 1] > 0:
            self.union(x, x + 1)
        if tmp and self.cnt[self.target] == 0:
            return True
        return False
