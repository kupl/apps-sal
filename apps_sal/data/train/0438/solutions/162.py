from collections import defaultdict


class Solution:

    def merge(self, x, y, f):
        f[y] = x
        t = y
        while f[t] != t:
            t = f[t]
        l = y
        while f[l] != l:
            (f[l], l) = (t, f[l])
        self.d[self.len[t]] -= 1
        self.d[self.len[y]] -= 1
        self.len[t] += self.len[y]
        self.d[self.len[t]] += 1

    def findLatestStep(self, arr: List[int], m: int) -> int:
        self.d = defaultdict(int)
        self.f = list(range(len(arr)))
        self.len = [0] * len(arr)
        state = [0] * len(arr)
        ans = -1
        for (i, num) in enumerate(arr):
            num = num - 1
            self.len[num] = 1
            self.d[1] += 1
            if num > 0 and state[num - 1] == 1:
                self.merge(num - 1, num, self.f)
            if num < len(arr) - 1 and state[num + 1]:
                self.merge(num, num + 1, self.f)
            state[num] = 1
            if m in self.d and self.d[m] > 0:
                ans = i + 1
        return ans
