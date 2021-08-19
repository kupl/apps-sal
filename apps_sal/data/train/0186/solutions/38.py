def cmp(s, t):
    if len(s) != len(t):
        return len(s) < len(t)
    for i in range(len(s)):
        if s[i] != t[i]:
            return s[i] < t[i]
    return False


class Solution:

    def largestNumber(self, cost: List[int], target: int) -> str:
        best = {}
        for i in range(len(cost) - 1, -1, -1):
            digit = i + 1
            if cost[i] not in best:
                best[cost[i]] = digit
        keys = sorted(list(best.keys()), key=lambda x: best[x], reverse=True)

        @lru_cache(None)
        def f(t, idx):
            if t == 0:
                return ''
            if t < 0 or idx == len(keys):
                return '0'
            k = keys[idx]
            b = '0'
            best_ct = 0
            for ct in range(t // k, -1, -1):
                r = f(t - k * ct, idx + 1)
                if r != '0':
                    if b == '0' or ct + len(r) > best_ct + len(b):
                        b = r
                        best_ct = ct
            return str(best[k]) * best_ct + b
        return f(target, 0)
