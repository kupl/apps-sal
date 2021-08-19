from functools import lru_cache
from itertools import takewhile


class Solution:
    def findGoodStrings(self, n: int, A: str, B: str, evil: str) -> int:
        MOD = 10 ** 9 + 7

        evil_checker = KMPTable(evil)

        @lru_cache(None)
        def DP(i=0, startswith_A=True, startswith_B=True, match_evil=0):
            # # <= s and not startwsith evil[e:]
            if match_evil == len(evil):
                return 0
            if i == n:
                return 1

            start = A[i] if startswith_A else 'a'
            end = B[i] if startswith_B else 'z'

            return sum(
                DP(
                    i + 1,
                    startswith_A and c == A[i],
                    startswith_B and c == B[i],
                    match_evil=evil_checker.match(c, idx=match_evil),
                )
                for c in map(chr, list(range(ord(start), ord(end) + 1)))
            ) % MOD

        return DP()


class KMPTable:

    def __init__(self, s):
        self.s = s
        self._init_table()

    def _init_table(self):
        self.table = [0, 0]
        for i in range(1, len(self.s)):
            self.table.append(
                self.match(self.s[i], idx=self.table[-1]),
            )

    def match(self, c, idx):
        if c == self.s[idx]:
            return idx + 1
        return self.match(c, self.table[idx]) if idx > 0 else 0
