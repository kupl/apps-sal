import numpy as np
import sys
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines

N = int(input())
X, Y = [], []
for _ in range(N):
    tx, ty = list(map(int, input().split()))
    X.append(tx)
    Y.append(ty)
X = np.array(X)
Y = np.array(Y)


def dist(cx, cy):
    tmp = ((X - cx) ** 2 + (Y - cy) ** 2) ** .5
    return max(tmp)


def g(cx):
    ll, rr = 0, 1000

    for _ in range(80):
        cll = (ll * 2 + rr) / 3
        crr = (ll + rr * 2) / 3
        if dist(cx, cll) >= dist(cx, crr):
            ll = cll
        else:
            rr = crr
    return dist(cx, ll)


l, r = 0, 1000

for _ in range(80):
    cl = (l * 2 + r) / 3
    cr = (l + r * 2) / 3
    if g(cl) >= g(cr):
        l = cl
    else:
        r = cr

ans = g(l)

print(ans)
