class Solution:
    def longestDupSubstring(self, S: str) -> str:

        arr = [ord(ch) - ord('a') for ch in S]
        n = len(arr)
        B = 29
        mod = 2**63 - 1

        def exists(L):
            seen = {}
            P = pow(B, L, mod)
            h = 0
            for i in range(n):
                h = (h * B + arr[i]) % mod
                if i >= L:
                    h = (h - arr[i - L] * P) % mod
                if i >= L - 1:
                    if h in seen:
                        return seen[h]
                    seen[h] = i
            return -1

        lo, hi = 0, len(S)
        pos = -1
        while lo < hi:
            mid = (lo + hi + 1) // 2
            idx = exists(mid)
            if idx != -1:
                lo = mid
                pos = idx
            else:
                hi = mid - 1
        return S[pos - lo + 1:pos + 1]
