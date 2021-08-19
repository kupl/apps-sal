class Solution:

    def longestDupSubstring(self, S: str) -> str:

        def check(Val):
            (base, modulus) = (26, 2 ** 32)
            AL = base ** Val % modulus
            hk = 0
            for i in range(Val):
                hk = hk * base + ord(S[i]) - ord('a')
            hk %= modulus
            hm = {hk: 0}
            for i in range(Val, N):
                hk = hk * base - (ord(S[i - Val]) - ord('a')) * AL + ord(S[i]) - ord('a')
                hk %= modulus
                if hk in hm and S[hm[hk]:hm[hk] + Val] == S[i - Val + 1:i + 1]:
                    return i - Val + 1
                hm[hk] = i - Val + 1
        N = len(S)
        (start, end) = (1, N)
        res = 0
        while start <= end:
            mid = start + (end - start) // 2
            pos = check(mid)
            if pos:
                res = pos
                start = mid + 1
            else:
                end = mid - 1
        return S[res:res + end]
