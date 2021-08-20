class Solution:

    def longestDupSubstring(self, S: str) -> str:

        def check(L):
            base = 26
            modulo = 2 ** 32
            AL = base ** L % modulo
            hk = 0
            for i in range(L):
                hk = hk * base + nums[i]
            hk %= modulo
            hm = {hk: 0}
            for i in range(L, len(S)):
                hk = (hk * base - nums[i - L] * AL + nums[i]) % modulo
                if hk in hm and S[i - L + 1:i + 1] == S[hm[hk]:hm[hk] + L]:
                    return i - L + 1
                hm[hk] = i - L + 1
            return -1
        nums = [ord(c) - ord('a') for c in S]
        res = -1
        (s, e) = (1, len(S))
        while s <= e:
            m = s + (e - s) // 2
            pos = check(m)
            if pos != -1:
                res = pos
                s = m + 1
            else:
                e = m - 1
        return S[res:res + e]
