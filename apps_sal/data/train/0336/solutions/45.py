class Solution:

    def minSteps(self, s: str, t: str) -> int:
        if s == t:
            return 0
        s_count = Counter(s)
        t_count = Counter(t)
        c = 0
        for (i, j) in s_count.items():
            if i in t_count:
                if t_count[i] < j:
                    c += j - t_count[i]
            else:
                c += j
        return c
