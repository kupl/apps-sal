import sys
import os


def f():
    return list(map(int, input().split()))


if 'local' in os.environ:
    sys.stdin = open('./input.txt', 'r')


def solve():
    n = f()[0]
    t = f()
    v = f()
    sumt = sum(t) * 2
    vs = [100000000] * (sumt + 1)
    vs[0] = 0
    for i in range(1, sumt):
        totalt = 0
        idx = 0
        for k in range(n):
            totalt += t[k] * 2
            if totalt >= i:
                idx = k
                break
        vs[i] = min(vs[i - 1] + 0.5, v[idx])
    vs[sumt] = 0
    for i in range(sumt - 1, 0, -1):
        totalt = 0
        idx = 0
        for k in range(n):
            totalt += t[k] * 2
            if totalt >= i + 1:
                idx = k
                break
        vs[i] = min(vs[i + 1] + 0.5, vs[i], v[idx])
    ans = 0
    for i in range(sumt):
        ans += (vs[i] + vs[i + 1]) / 4
    print(ans)


solve()
