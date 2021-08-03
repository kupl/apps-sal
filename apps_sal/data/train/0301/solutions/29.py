class Solution:
    def getMaxUncrossedLinesFrom(self, A, B, min_a_ix, min_b_ix):
        max_count = 0
        key = (min_a_ix, min_b_ix)
        if key in self.cache:
            return self.cache[key]

        for i_a in range(min_a_ix, len(A)):
            val_a = A[i_a]
            b_match_indexes = self.b_lookup.get(val_a)
            if not b_match_indexes:
                continue
            for b_ix in b_match_indexes:
                if b_ix >= min_b_ix:
                    ct = 1 + self.getMaxUncrossedLinesFrom(A, B, i_a + 1, b_ix + 1)
                    max_count = max(max_count, ct)
        self.cache[key] = max_count
        return max_count

    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        b_lookup = defaultdict(list)
        for i, n in enumerate(B):
            b_lookup[n].append(i)
        self.b_lookup = b_lookup
        self.cache = {}

        return self.getMaxUncrossedLinesFrom(A, B, 0, 0)
