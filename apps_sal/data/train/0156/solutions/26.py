class Solution:

    def shortestCommonSupersequence(self, s1: str, s2: str) -> str:
        m = {}

        def fs(a, b):
            if (a, b) in list(m.keys()):
                return m[a, b]
            if a == len(s1) or b == len(s2):
                m[a, b] = ''
                return ''
            if s1[a] == s2[b]:
                r = s1[a] + fs(a + 1, b + 1)
                return r
            r1 = fs(a + 1, b)
            r2 = fs(a, b + 1)
            if len(r1) > len(r2):
                m[a, b] = r1
            else:
                m[a, b] = r2
            return m[a, b]
        r = fs(0, 0)
        res = ''
        (i, j) = (0, 0)
        for a in r:
            while i < len(s1) and s1[i] != a:
                res += s1[i]
                i += 1
            i += 1
            while j < len(s2) and s2[j] != a:
                res += s2[j]
                j += 1
            j += 1
            res += a
        res += s1[i:] + s2[j:]
        return res
