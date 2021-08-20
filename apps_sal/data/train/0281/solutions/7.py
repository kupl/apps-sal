class Solution:

    def canConvertString(self, s: str, t: str, k: int) -> bool:
        d = {}
        m1 = [0, 0]
        n = len(s)
        if len(t) != n:
            return False
        for i in range(n):
            diff = (ord(t[i]) - ord(s[i])) % 26
            if diff != 0:
                if diff not in d:
                    d[diff] = 0
                d[diff] += 1
                m1 = max(m1, [d[diff], diff])
        m2 = 26 * (m1[0] - 1) + m1[1]
        return k >= m2
