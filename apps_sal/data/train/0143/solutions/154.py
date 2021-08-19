class Solution:

    def totalFruit(self, t: List[int]) -> int:
        (st, a, b, a_hi, res, b_hi) = (0, t[0], -1, 0, 0, 0)
        for (i, v) in enumerate(t):
            if v != a and b == -1:
                b = v
                b_hi = i
            elif v == a:
                a_hi = i
            elif v == b:
                b_hi = i
            elif v not in (a, b):
                res = max(res, i - st)
                st_m = min(a_hi, b_hi)
                (a, b, st, a_hi, b_hi) = (t[st_m + 1], v, st_m + 1, max(a_hi, b_hi), i)
        return max(res, len(t) - st)
