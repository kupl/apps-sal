from collections import defaultdict
from functools import lru_cache


class Solution:

    @lru_cache(None, False)
    def solve(self, a_from: int, b_from: int):
        if a_from >= len(self.A) or b_from >= len(self.B):
            return 0
        else:
            max_line = 0
            for b_pos in self.b_index[self.A[a_from]]:
                if b_pos >= b_from:
                    if_draw = 1 + self.solve(a_from + 1, b_pos + 1)
                    max_line = max(max_line, if_draw)
            max_line = max(self.solve(a_from + 1, b_from), max_line)
            return max_line

    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        self.A = A
        self.B = B
        self.b_index = defaultdict(list)
        for (i, b) in enumerate(B):
            self.b_index[b].append(i)
        return self.solve(0, 0)
