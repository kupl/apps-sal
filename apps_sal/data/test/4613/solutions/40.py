from collections import deque
from sys import stdin
input = stdin.readline


class Unionfind():
    def __init__(self, n):
        self.n = n
        self.parent = [-1] * n

    def find(self, x):
        if self.parent[x] < 0:
            return x
        else:
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return
        if self.parent[x] < self.parent[y]:
            x, y = y, x

        self.parent[x] += self.parent[y]
        self.parent[y] = x


N, M = map(int, input().split())
A = [-1] * M; B = [-1] * M
for i in range(M):
    a, b = map(lambda x: int(x) - 1, input().split())
    A[i] = a; B[i] = b

ans = 0
for exclude_idx in range(M):
    uf = Unionfind(N)
    for i in range(M):
        if i == exclude_idx:
            continue
        uf.union(A[i], B[i])

    cnt = 0
    for parent in uf.parent:
        if parent < 0:
            cnt += 1
    if cnt >= 2:
        ans += 1

print(ans)
