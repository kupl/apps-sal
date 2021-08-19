import itertools as it


def dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def spir_dist(x):
    (a, b) = x
    if a >= b:
        return b
    else:
        return 2 * b - a


n = int(input())
A = [[0, 0]]
for _ in range(n):
    (x, y) = list(map(int, input().split()))
    A += [[x, y]]
A_s = sorted(A, key=max)
A_g = it.groupby(A_s, key=max)
A_t = [p + p if len(p) == 1 else [p[0], p[-1]] for p in [sorted(list(q[1]), key=spir_dist) for q in A_g]]
B = [[0, 0]]
for i in range(1, len(A_t)):
    (pa, pb) = A_t[i]
    d = dist(pa, pb)
    y = min([B[i - 1][k] + dist(A_t[i - 1][k], pa) for k in [0, 1]]) + d
    x = min([B[i - 1][k] + dist(A_t[i - 1][k], pb) for k in [0, 1]]) + d
    B += [[x, y]]
print(min(B[len(A_t) - 1]))
