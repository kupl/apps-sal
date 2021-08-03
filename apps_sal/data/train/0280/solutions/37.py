class Solution:
    def cost(self, i, j):
        if i + 1 >= j:
            return 0
        if i + 2 == j:
            return 0 if self.s[i] == self.s[j - 1] else 1

        try:
            return self.cost_cache[(i, j)]
        except KeyError:
            ret = self.cost(i + 1, j - 1) + (0 if self.s[i] == self.s[j - 1] else 1)
            self.cost_cache[(i, j)] = ret
            return ret

    def num_changes(self, i, kk):
        rem_len = len(self.s) - i
        if rem_len < kk:
            return self.MAX
        if rem_len == kk:
            return 0
        if kk == 1:
            return self.cost(i, len(self.s))

        try:
            return self.num_changes_cache[(i, kk)]
        except KeyError:
            ret = self.MAX
            for j in range(i + 1, len(self.s) - (kk - 1) + 1):
                ret = min(ret, self.cost(i, j) + self.num_changes(j, kk - 1))
            self.num_changes_cache[(i, kk)] = ret
            return ret

    def palindromePartition(self, s: str, k: int) -> int:
        self.s = s
        self.MAX = len(s)
        self.cost_cache = {}
        self.num_changes_cache = {}

        for l in range(3, len(s)):
            for i in range(len(s) - l + 1):
                j = i + l
                self.cost(i, j)
        for i in range(len(s) - 3, -1, -1):
            for kk in range(2, min(len(s) - i - 1, k - 1) + 1):
                self.num_changes(i, kk)

        return self.num_changes(0, k)
