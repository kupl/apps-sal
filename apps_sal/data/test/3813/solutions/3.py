
from itertools import chain, product

N = int(input())

P = list(chain((0,), [int(x) - 1 for x in input().split()]))
X = list(map(int, input().split()))

L = [list() for _ in range(N)]

debug = [None] * N

for i in reversed(list(range(N))):
    p = P[i]
    l = L[i]

    x = X[i]

    # len(l) < 10のとき全探索、それ以上はDP
    if len(l) < 10:
        m = -1
        for s in product(*l):
            n = sum(s)
            if n <= x:
                m = max(n, m)
        if m == -1:
            print('IMPOSSIBLE')
            return
        m = sum(chain.from_iterable(l)) - m
    else:
        offset = sum(min(t) for t in l)
        x -= offset
        if x < 0:
            print('IMPOSSIBLE')
            return
        dp = [False] * (x + 1)
        dp[0] = True
        s = 0
        for a, b in l:
            d = abs(a - b)
            s += d
            for j in reversed(list(range(x - d + 1))):
                dp[j + d] = dp[j + d] or dp[j]
        m = x
        while not dp[m]:
            m -= 1
        m = s - m
        m += offset
        x += offset

    debug[i] = (x, m)
    L[p].append((x, m))
    L[i] = None

print('POSSIBLE')
