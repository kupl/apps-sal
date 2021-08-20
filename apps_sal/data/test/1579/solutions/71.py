import sys
from bisect import bisect_left


def sr():
    return sys.stdin.readline().rstrip()


def ir():
    return int(sr())


def lr():
    return list(map(int, sr().split()))


N = ir()
XY = [lr() for _ in range(N)]
V = list(range(2 * 10 ** 5 + 1))


def find(A, x):
    p = A[x]
    if p == x:
        return x
    a = find(A, p)
    A[x] = a
    return a


def union(A, x, y):
    if find(A, x) > find(A, y):
        (bx, by) = (find(A, y), find(A, x))
    else:
        (bx, by) = (find(A, x), find(A, y))
    A[by] = bx


for (x, y) in XY:
    y += 10 ** 5
    if find(V, x) != find(V, y):
        union(V, x, y)
set_V = [set() for _ in range(2 * 10 ** 5 + 1)]
for (x, y) in XY:
    root = find(V, x)
    set_V[root] |= set([x, y + 10 ** 5])
set_V = [x for x in set_V if x]
answer = 0
for z in set_V:
    z = sorted(list(z))
    cnt_x = bisect_left(z, 10 ** 5 + 1)
    cnt_y = len(z) - cnt_x
    answer += cnt_x * cnt_y
answer -= N
print(answer)
