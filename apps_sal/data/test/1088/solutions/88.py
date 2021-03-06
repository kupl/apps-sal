import math
(N, K) = list(map(int, input().split()))
A = []
mod = 998244353
for _ in range(N):
    A.append(list(map(int, input().split())))


def find(x, uf):
    if uf[x] != x:
        uf[x] = find(uf[x], uf)
    return uf[x]


def union(x, y, uf, rank):
    (px, py) = (find(x, uf), find(y, uf))
    if px != py:
        if rank[px] > rank[py]:
            (px, py) = (py, px)
        rank[py] += rank[px]
        uf[px] = py


uf1 = {i: i for i in range(N)}
uf2 = {i: i for i in range(N)}
rank1 = {i: 1 for i in range(N)}
rank2 = {i: 1 for i in range(N)}
for i in range(N):
    for j in range(i + 1, N):
        if all((a + b <= K for (a, b) in zip(A[i], A[j]))):
            (px, py) = (find(i, uf1), find(j, uf1))
            if px != py:
                if rank1[px] > rank1[py]:
                    (px, py) = (py, px)
                rank1[py] += rank1[px]
                uf1[px] = py
B = list(zip(*A))
for i in range(N):
    for j in range(i + 1, N):
        if all((a + b <= K for (a, b) in zip(B[i], B[j]))):
            (px, py) = (find(i, uf2), find(j, uf2))
            if px != py:
                if rank2[px] > rank2[py]:
                    (px, py) = (py, px)
                rank2[py] += rank2[px]
                uf2[px] = py
ans = 1
for x in set((find(i, uf1) for i in range(N))):
    ans *= math.factorial(rank1[x])
    ans %= mod
for x in set((find(i, uf2) for i in range(N))):
    ans *= math.factorial(rank2[x])
    ans %= mod
print(ans)
