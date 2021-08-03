from bisect import bisect_left as bl, bisect_right as br
from operator import itemgetter
import sys
def input(): return sys.stdin.readline().rstrip()


sys.setrecursionlimit(max(1000, 10**9))
def write(x): return sys.stdout.write(x + "\n")


n, m = list(map(int, input().split()))
w = list(map(int, input().split()))
lv = []
lm = -1
for i in range(m):
    lv.append(tuple(map(int, input().split())))
    lm = max(lm, lv[-1][0])
lv.sort(key=itemgetter(1))
nlv = [(0, 0), lv[0]]
for l, v in lv:
    if l <= nlv[-1][0]:
        continue
    nlv.append((l, v))
vs = [nlv[i][1] for i in range(len(nlv))]


def sub(x):
    ind = bl(vs, x - 0.5)
    if ind == 0:
        return 0
    return nlv[ind - 1][0]


def cumsum(a):
    """※ aを破壊する
    l[i] = sum(a[:i]) なるlを返す
    sum(a[i:j]) == l[j+1] - l[i]
    """
    c = 0
    n = len(a)
    a.insert(0, 0)
    for i in range(1, n + 1):
        a[i] = a[i - 1] + a[i]
    return a


if nlv[-1][1] < max(w):
    ans = -1
else:
    from itertools import permutations
    l = list(range(n))
    ans = float("inf")
    for ps in permutations(l):
        cum = cumsum([w[ps[i]] for i in range(n)])
        if sub(cum[1]) == float("inf"):
            continue
        ls = [0]
        for i in range(1, n):
            #         val = ls[i-1]+lm
            val = max(ls[ii] + sub(cum[i + 1] - cum[ii]) for ii in range(i))
            ls.append(val)
        ans = min(ans, ls[-1])
    if ans > 10**20:
        ans = -1
print(ans)
