import sys


def input():
    return sys.stdin.readline()[:-1]


(H, W, N) = map(int, input().split())
d = {}
for i in range(N):
    (a, b) = map(int, input().split())
    for j in range(-1, 2):
        if not 1 < a + j < H:
            continue
        for k in range(-1, 2):
            if not 1 < b + k < W:
                continue
            t = (a + j, b + k)
            if t in d:
                d[t] += 1
            else:
                d[t] = 1
l = [0] * 10
for i in d.values():
    l[i] += 1
l[0] = (H - 2) * (W - 2) - sum(l)
print(*l, sep='\n')
