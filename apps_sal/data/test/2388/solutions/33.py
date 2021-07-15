
M = 998244353

n = int(input())
xs = [0] * n
ds = [0] * n
for i in range(n):
    x, d = (int(c) for c in input().split())
    ds[i] = d
    xs[i] = (x,i)

import sys
sys.setrecursionlimit(max(1000,n))

xs.sort()
index = [x[1] for x in xs]
xs = [x[0] for x in xs]
ds = [ds[ind] for ind in index]

def _sub(i):
    # 深さ優先探索しながらi番目以下の組み合わせと、次に調べるべき番号を返す
    if i==n-1:
        return 2, n
    res = 1
    ind = i+1
    while True:
        if (xs[i]+ds[i] <= xs[ind]):
            break
        o, ind = _sub(ind)
        res *= o
        res %= M
        if ind>=n:
            break
    return res+1, ind
out = []
done = 0
while True:
    o, done = _sub(done)
    out.append(o)
    if done>=n:
        break
result = 1
for o in out:
    result *= o
    result %= M
print(result)
