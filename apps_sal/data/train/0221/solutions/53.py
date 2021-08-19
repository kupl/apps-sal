class Solution:

    def longestDupSubstring(self, S: str) -> str:
        ords = [ord(ch) - 97 for ch in S]
        mod = 2 ** 32
        seen = set()

        def has_dup_with_length(length):
            seen.clear()
            p = pow(26, length, mod)
            hashed_prefix = 0
            for i in range(length):
                hashed_prefix = (hashed_prefix * 26 + ords[i]) % mod
            seen.add(hashed_prefix)
            for i in range(length, len(S)):
                hashed_prefix = (hashed_prefix * 26 + ords[i] - ords[i - length] * p) % mod
                if hashed_prefix in seen:
                    return i - length + 1
                seen.add(hashed_prefix)
        (start, lo, hi) = (0, 0, len(S) - 1)
        while lo < hi:
            mid_length = (lo + hi + 1) // 2
            idx = has_dup_with_length(mid_length)
            if idx:
                start = idx
                lo = mid_length
            else:
                hi = mid_length - 1
        return S[start:start + lo]
