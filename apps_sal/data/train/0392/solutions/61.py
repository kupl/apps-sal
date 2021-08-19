class Solution:

    def numWays(self, s: str) -> int:
        (N, ones) = (len(s), 0)
        for c in s:
            ones += 1 if c == '1' else 0
        if ones % 3 == 1:
            return 0
        if ones == 0:
            return ((N - 1) * (N - 2) >> 1) % (10 ** 9 + 7)
        want = ones // 3
        (c1, c2) = (0, 0)
        (p, suff) = (0, 0)
        for c in s:
            if c == '1':
                c1 += 1
            if c1 == want:
                p += 1
        for c in reversed(s):
            if c == '1':
                c2 += 1
            if c2 == want:
                suff += 1
        return p * suff % (10 ** 9 + 7)
