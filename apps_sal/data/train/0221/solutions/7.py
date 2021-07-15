from functools import reduce
class Solution:
    def longestDupSubstring(self, S: str) -> str:
        A = [ord(c) - ord('a') for c in S]
        mod = 2**63 - 1
        
        def test(L):
            p = pow(26, L, mod)
            cur = reduce(lambda x, y: (x * 26 + y) % mod, A[: L], 0)
            seen = set()
            seen.add(cur)
            for i in range(L, len(A)):
                cur = (cur * 26 + A[i] - A[i - L] * p) % mod
                if cur in seen:
                    return i - L + 1
                seen.add(cur)
        
        res, lo, hi = 0, 0, len(S)
        while lo + 1 < hi:
            mid = lo + (hi - lo) // 2
            pos = test(mid)
            if pos:
                lo = mid
            else:
                hi = mid
        
        if test(hi):
            pos = test(hi)
            return S[pos: pos + hi]
        pos = test(lo)
        return S[pos: pos + lo]

