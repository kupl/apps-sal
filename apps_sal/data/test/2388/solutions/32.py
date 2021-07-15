# hmm...
from sys import setrecursionlimit
setrecursionlimit(10000000)

n = int(input())
xds = [tuple(map(int, input().split())) for _ in range(n)]
xds.sort()

xds.insert(0, (-1000000001, 2000000004))
n += 1

def make_blocks(i):
    x, d = xds[i]
    right = x + d
    res = []
    nexti = i + 1
    while(nexti < n):
        xn, dn = xds[nexti]
        if xn < right:
            l, lasti = make_blocks(nexti)
            res.append(l)
            nexti = lasti + 1
        else:
            return res, nexti - 1
    return res, n - 1

l, _ = make_blocks(0)

def count(l):
    ans = 1
    for ll in l:
        ans = ans * (1 + count(ll)) % 998244353
    return ans

print((count(l)))

