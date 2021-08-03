# solution
import io
import math
import string


def col(n, m):
    X = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        X[a - 1].append(b - 1)
        X[b - 1].append(a - 1)
    C = [-1] * n
    c = 0
    for i in range(N):
        if C[i] >= 0:
            continue
        Q = [i]
        C[i] = c
        while Q:
            x = Q.pop()
            for y in X[x]:
                if C[y] == -1:
                    C[y] = C[x]
                    Q.append(y)
        c += 1
    return C


N, K, L = map(int, input().split())
A = col(N, K)
B = col(N, L)
D = {}
for a, b in zip(A, B):
    t = (a << 18) + b
    if t in D:
        D[t] += 1
    else:
        D[t] = 1

print(*[D[(a << 18) + b] for a, b in zip(A, B)])
