from functools import reduce


class Solution:

    def longestDupSubstring(self, S: str) -> str:
        from functools import reduce
        A = [ord(c) - ord('a') for c in S]
        mod = 2 ** 63 - 1

        def judge(l):
            p = 26 ** l % mod
            cur = reduce(lambda x, y: (x * 26 + y) % mod, A[:l], 0)
            seen = {cur}
            for i in range(l, len(S)):
                cur = (cur * 26 + A[i] - p * A[i - l]) % mod
                if cur in seen:
                    return i - l + 1
                seen.add(cur)
        (lo, hi) = (0, len(S))
        res = 0
        while lo < hi:
            mi = (lo + hi + 1) // 2
            pos = judge(mi)
            if pos:
                lo = mi
                res = pos
            else:
                hi = mi - 1
        return S[res:res + lo]
