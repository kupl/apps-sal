class Solution:
    def longestPrefix(self, s: str) -> str:
        M = 19134702400093278081449423917
        n, h, t = len(s), 0, 0
        v = list(map(lambda x: ord(x) - ord('a'), s))
        l, p = 0, 1
        for i in range(n - 1):
            h = (h * 26 + v[i]) % M
            t = (v[n - 1 - i] * p + t) % M
            p = p * 26 % M
            if h == t:
                l = i + 1
        return s[:l]
