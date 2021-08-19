from collections import defaultdict
import itertools
d = defaultdict(int)
x = 'MARCH'
for i in range(5):
    d[x[i]] = i + 1
x = [0] * 5


def sub(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


(H, W, D) = map(int, input().split())
A = [list(map(int, input().split())) for i in range(H)]
N = H * W
P = [0] * N
for h in range(H):
    for w in range(W):
        P[A[h][w] - 1] = (h, w)
X = []
for d in range(D):
    _ = [0] + [sub(P[i % N], P[i - D]) for i in range(d + D, N + D, D)]
    cumsum = list(itertools.accumulate(_))
    X.append(cumsum)
Q = int(input())
for q in range(Q):
    (l, r) = map(int, input().split())
    (l, r) = (l - 1, r - 1)
    g = l % D
    if l > r:
        r += N
        ans = X[g][-1] - X[g][l // D]
        ans += X[g][r // D] - X[g][0]
    else:
        ans = X[g][r // D] - X[g][l // D]
    print(ans)
