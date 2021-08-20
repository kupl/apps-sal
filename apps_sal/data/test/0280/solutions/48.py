from bisect import bisect_left
from itertools import permutations
from operator import itemgetter


def solve(n, m, www, lv):
    lv.sort(key=itemgetter(1))
    if lv[0][1] < max(www):
        return -1
    lll = [0]
    vvv = [0]
    for (l, v) in lv:
        if v == vvv[-1]:
            lll[-1] = max(lll[-1], l)
        elif l > lll[-1]:
            lll.append(l)
            vvv.append(v)
    ans = 10 ** 18
    for order in permutations(list(range(n))):
        dists = [0] * n
        for oi in range(n - 1):
            d = dists[oi]
            total_weight = www[order[oi]]
            for oj in range(oi + 1, n):
                total_weight += www[order[oj]]
                k = bisect_left(vvv, total_weight) - 1
                dists[oj] = max(dists[oj], d + lll[k])
        ans = min(ans, dists[-1])
    return ans


(n, m) = list(map(int, input().split()))
www = list(map(int, input().split()))
lv = [tuple(map(int, input().split())) for _ in range(m)]
ans = solve(n, m, www, lv)
print(ans)
