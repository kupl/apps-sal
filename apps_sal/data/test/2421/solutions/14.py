import sys


def input(): return sys.stdin.readline().strip()
def list2d(a, b, c): return [[c for j in range(b)] for i in range(a)]
def list3d(a, b, c, d): return [[[d for k in range(c)] for j in range(b)] for i in range(a)]
def list4d(a, b, c, d, e): return [[[[e for l in range(d)] for k in range(c)] for j in range(b)] for i in range(a)]
def ceil(x, y=1): return int(-(-x // y))
def INT(): return int(input())
def MAP(): return list(map(int, input().split()))
def LIST(N=None): return list(MAP()) if N is None else [INT() for i in range(N)]
def Yes(): print('Yes')
def No(): print('No')
def YES(): print('YES')
def NO(): print('NO')


INF = 10**19
MOD = 10**9 + 7
EPS = 10**-10

for _ in range(INT()):
    gy, gx = MAP()
    C = LIST()

    C[5] = min(C[5], C[0] + C[4])
    C[1] = min(C[1], C[0] + C[2])
    C[2] = min(C[2], C[3] + C[1])
    C[4] = min(C[4], C[3] + C[5])
    C[5] = min(C[5], C[0] + C[4])
    C[1] = min(C[1], C[0] + C[2])
    C[2] = min(C[2], C[3] + C[1])
    C[4] = min(C[4], C[3] + C[5])

    ans = 0
    if gx > 0 and gy > 0:
        mn = min(gx, gy)
        ans += mn * min(C[1] + C[5], C[0])
        if gx > gy:
            ans += (gx - mn) * C[1]
        elif gx < gy:
            ans += (gy - mn) * C[5]
    elif gx < 0 and gy < 0:
        gx, gy = abs(gx), abs(gy)
        mn = min(gx, gy)
        ans += mn * min(C[2] + C[4], C[3])
        if gx > gy:
            ans += (gx - mn) * C[4]
        elif gx < gy:
            ans += (gy - mn) * C[2]
    else:
        if gx < 0:
            ans += abs(gx) * C[4]
        elif gx > 0:
            ans += gx * C[1]
        if gy < 0:
            ans += abs(gy) * C[2]
        elif gy > 0:
            ans += gy * C[5]
    print(ans)
