from collections import deque
import sys


def input():
    return sys.stdin.readline().rstrip()


N = int(input())
X = [[] for _ in range(N)]
for _ in range(N - 1):
    (a, b) = map(int, input().split())
    X[a - 1].append(b - 1)
    X[b - 1].append(a - 1)


def farthest(i):
    L = [-1] * N
    L[i] = 0
    d = 0
    post = [i]
    while len(post) > 0:
        d += 1
        pre = post
        post = []
        for j in pre:
            for k in X[j]:
                if L[k] < 0:
                    L[k] = d
                    post.append(k)
    return (pre[0], d - 1)


(s, _) = farthest(0)
(t, d) = farthest(s)


def BFS_dist(n, E, i0=0):
    Q = deque([i0])
    D = [-1] * n
    D[i0] = 0
    while Q:
        x = Q.popleft()
        for c in E[x]:
            if D[c] == -1:
                D[c] = D[x] + 1
                Q.append(c)
    return D


D1 = BFS_dist(N, X, s)
D2 = BFS_dist(N, X, t)
Y = [0] * (d + 1)
ma = 0
for i in range(N):
    if i == s or i == t:
        continue
    (a, b) = sorted((D1[i], D2[i]))
    ma = max(ma, a)
    Y[b] += 1
Y[d] += 1
P = 10 ** 9 + 7
i2 = P + 1 >> 1
s = 1
ans = d
for i in range(d, ma, -1):
    if Y[i]:
        s = pow(i2, Y[i], P) * s % P
    ans -= s
    if ans < 0:
        ans += P
print(ans * pow(2, N, P) % P)
