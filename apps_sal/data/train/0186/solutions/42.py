def cmp(a, b):
    (ad, bd) = ({}, {})
    for i in range(0, len(a), 2):
        ad[a[i]] = a[i + 1]
    for i in range(0, len(b), 2):
        bd[b[i]] = b[i + 1]
    sad = sum(ad.values())
    sbd = sum(bd.values())
    if sad != sbd:
        return sad < sbd
    al = sorted(list(ad.keys()), reverse=True)
    bl = sorted(list(bd.keys()), reverse=True)
    for i in range(1 + min(len(al), len(bl))):
        if al[i] == bl[i]:
            c = al[i]
            if ad[c] != bd[c]:
                return ad[c] < bd[c]
        else:
            return al[i] < bl[i]
    return False


class Solution:

    def largestNumber(self, cost: List[int], target: int) -> str:
        best = {}
        for i in range(len(cost) - 1, -1, -1):
            digit = i + 1
            if cost[i] not in best:
                best[cost[i]] = digit
        x = sorted(best.keys())
        y = sorted(list(best.values()), reverse=True)

        @lru_cache(None)
        def best_path(t, idx):
            if t == 0:
                return tuple()
            if idx == len(x):
                return None
            ret = None
            bi = -1
            for i in range(t // x[idx], -1, -1):
                y = best_path(t - i * x[idx], idx + 1)
                if y is not None:
                    if i > 0:
                        y = (best[x[idx]], i) + y
                    if bi == -1 or cmp(ret, y):
                        ret = y
                        bi = i
            return ret
        r = best_path(target, 0)
        if r is None:
            return '0'
        unpacked = {}
        for i in range(0, len(r), 2):
            unpacked[r[i]] = r[i + 1]
        s = ''
        for digit in y:
            if digit in unpacked:
                s += str(digit) * unpacked[digit]
        return s
