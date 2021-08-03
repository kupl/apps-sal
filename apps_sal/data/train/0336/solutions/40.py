class Solution:
    def minSteps(self, s: str, t: str) -> int:

        result = len(s)
        for i in set(s):
            n_s = s.count(i)
            n_t = t.count(i)
            result = result - min(n_s, n_t)

        return result
