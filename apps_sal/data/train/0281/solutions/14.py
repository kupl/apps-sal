def shift(c, n):
    return chr(ord(c) + n % 26)


class Solution:

    def canConvertString(self, s: str, t: str, k: int) -> bool:
        if len(s) != len(t):
            return False
        d = {}
        mx = 0
        for i in range(len(s)):
            c1 = s[i]
            c2 = t[i]
            if c1 == c2:
                continue
            j = ord(c2) - ord(c1)
            j = j % 26
            if j not in d:
                d[j] = 1
            else:
                d[j] += 1
            mx = max(mx, (d[j] - 1) * 26 + j)
        return mx <= k
