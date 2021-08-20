from collections import deque
import sys
sys.setrecursionlimit(10 ** 7)
(N, u, v) = map(int, input().split())
D = [[] for i in range(N)]
for i in range(N - 1):
    (a, b) = map(int, input().split())
    a -= 1
    b -= 1
    D[a].append(b)
    D[b].append(a)
Taka = [0] * (N + 1)
Aoki = [0] * (N + 1)


def f(n, p, A):
    for i in D[n]:
        if i != p:
            A[i] = A[n] + 1
            f(i, n, A)


f(u - 1, -1, Taka)
f(v - 1, -1, Aoki)
ans = 0
for i in range(N):
    if Taka[i] < Aoki[i]:
        ans = max(ans, Aoki[i] - 1)
print(ans)
