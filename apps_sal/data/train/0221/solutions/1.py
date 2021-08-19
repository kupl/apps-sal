class Solution:

    def longestDupSubstring(self, S: str) -> str:

        def has_duplicate(m, S):
            (val, Mod) = (0, 2 ** 63 - 1)
            for i in range(m):
                val = (26 * val + ord(S[i])) % Mod
            d = set([val])
            const = 26 ** m % Mod
            for i in range(m, len(S)):
                val = (26 * val + ord(S[i]) - ord(S[i - m]) * const) % Mod
                if val in d:
                    return i - m + 1
                d.add(val)
            return -1
        (l, r) = (0, len(S))
        (start, length) = (-1, 0)
        while l <= r:
            mid = l + (r - l) // 2
            idx = has_duplicate(mid, S)
            if idx != -1:
                l = mid + 1
                (start, length) = (idx, mid)
            else:
                r = mid - 1
        if start == -1:
            return ''
        return S[start:start + length]
