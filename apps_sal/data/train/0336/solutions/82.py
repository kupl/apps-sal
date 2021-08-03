class Solution:
    def minSteps(self, s: str, t: str) -> int:
        D_s = {}
        D_t = {}
        for v in t:
            D_t[v] = 0
        for v in t:
            D_t[v] += 1
        for v in s:
            D_s[v] = 0
        for v in s:
            D_s[v] += 1
        S = 0
        U = set()
        for v in t:
            if v not in D_s:
                S += 1
            else:
                U.add(v)
        for u in U:
            S += max(D_t[u] - D_s[u], 0)
        return S
