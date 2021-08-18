class Solution:
    def lastSubstring(self, s: str) -> str:
        lastc = max(s)
        n = len(s)
        q = [i for i, val in enumerate(s) if val == lastc]
        if len(q) == len(s):
            return s
        res = s[q[0]]
        while q:
            qq = []
            for i in q:
                if i + 1 < n:
                    qq += [i + 1]
            if not qq:
                break
            c = max(s[i] for i in qq)
            res += c
            q = [i for i in qq if s[i] == c]

        return res

        return sorted(ans)[-1]
