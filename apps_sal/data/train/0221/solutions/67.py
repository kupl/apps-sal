class Solution:
    def longestDupSubstring(self, S: str) -> str:
        p = 31
        m = 100000000003

        pows = [1] * len(S)
        invPows = [1] * len(S)
        for i in range(1, len(S)):
            pows[i] = pows[i - 1] * p % m
            invPows[i] = pow(pows[i], -1, m)

        h = [0] * (len(S) + 1)
        for i in range(len(S)):
            h[i + 1] = (h[i] + (ord(S[i]) - ord('a') + 1) * pows[i]) % m

        def hasDup(S, sublen):
            seen = set()
            for i in range(len(S) - sublen + 1):
                if (hs := (h[i + sublen] - h[i]) * invPows[i] % m) in seen:
                    return (i, sublen)
                seen.add(hs)
            return (0, 0)

        ans = None
        lo, hi = 1, len(S)
        while lo < hi:
            mid = (lo + hi) // 2
            if (s := hasDup(S, mid))[1]:
                lo = mid + 1
                ans = s
            else:
                hi = mid
        return S[ans[0]:ans[0] + ans[1]] if ans else ''
