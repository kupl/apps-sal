from collections import deque

N = int(input())
xy = [list(map(int, input().split())) for _ in range(N)]


def dist(a, b):
    return pow(pow(b[0] - a[0], 2) + pow(b[1] - a[1], 2), 1 / 2)


que = deque([[i] for i in range(N)])
perm = []
while que:
    seq = que.popleft()
    if len(seq) == N:
        perm.append(seq)
    for j in range(N):
        if j not in seq:
            que.append(seq + [j])

d = 0
s = len(perm)
for p in perm:
    for k in range(N - 1):
        d += dist(xy[p[k]], xy[p[k + 1]])
print(d / s)
