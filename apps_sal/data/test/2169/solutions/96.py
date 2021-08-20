import sys


def calc(x):
    if x < D + 1:
        mv[x] = 0
        return 0
    else:
        p = d[x][0]
        q = d[x][1]
        r = d[x - D][0]
        s = d[x - D][1]
        tmp = abs(p - r) + abs(q - s)
        ret = tmp + calc(x - D)
        mv[x] = ret
        return ret


sys.setrecursionlimit(10 ** 5)
(H, W, D) = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
Q = int(input())
d = dict()
z = 0
for a in A:
    for b in a:
        p = z // W
        q = z % W
        d[b] = (p, q)
        z += 1
mv = [0] * (H * W + 1)
for i in range(D):
    calc(H * W - i)
L = [0] * Q
R = [0] * Q
for _ in range(Q):
    (L, R) = map(int, input().split())
    print(mv[R] - mv[L])
