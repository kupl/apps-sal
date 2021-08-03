from itertools import permutations, zip_longest
from collections import OrderedDict


class Solution:
    def isSolvable(self, words: List[str], result: str) -> bool:

        self.matched_chars = list(zip_longest(*[result[::-1]] + [w[::-1] for w in words]))
        self.first_chars = set([result[0]] + [w[0] for w in words])
        self.chars = []
        self.free_vars = []
        self.idx = {}
        observed = set()
        for chars in self.matched_chars:
            free_vars = []
            for c in chars:
                if c is None:
                    continue
                if c not in observed:
                    self.chars.append(c)
                    free_vars.append(c)
                    observed.add(c)
                    self.idx[c] = len(self.idx)
            self.free_vars.append(free_vars)
        # print(self.free_vars)
        # print(self.chars)

        return self.dfs(0, (), 0)

    # @lru_cache(maxsize=None)
    def dfs(self, i, used_digits, carry):
        # pemutations
        if i >= len(self.matched_chars):
            # print('R:',used_digits)
            return not max(used_digits[self.idx[f]] == 0 for f in self.first_chars)
        free_vars = self.free_vars[i]
        perms = permutations(set(range(10)) - set(list(used_digits)), len(free_vars))
        for p in perms:
            values = tuple(list(used_digits) + list(p))
            # check for contradiction
            nxt_carry = self.contradict(values, i, carry)
            if nxt_carry < 0:
                continue
            if self.dfs(i + 1, values, nxt_carry):
                return True
        return False

    def contradict(self, values, i, carry):
        r, *i = self.matched_chars[i]
        s = sum(values[self.idx[d]] for d in i if d) + carry
        if (s - values[self.idx[r]]) % 10:
            return -1
        return s // 10
