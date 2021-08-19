class Solution:

    def longestDupSubstring(self, S: str) -> str:
        A = [ord(c) for c in S]
        mod = 2 ** 63 - 1
        lo = 0
        hi = len(S)
        res = 0

        def test(sz):
            val = 0
            p = pow(26, sz, mod)
            for i in range(sz):
                val = val * 26 + A[i]
                val %= mod
            seen = {val}
            for i in range(sz, len(A)):
                val = val * 26 + A[i] - A[i - sz] * p
                val = val % mod
                if val in seen:
                    return i - sz + 1
                seen.add(val)
            return -1
        while lo < hi:
            mid = (lo + hi) // 2
            pos = test(mid)
            if not pos >= 0:
                hi = mid
            else:
                res = pos
                lo = mid + 1
        return S[res:res + lo - 1]
