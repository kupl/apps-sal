from sys import stdin, setrecursionlimit
input = stdin.readline
setrecursionlimit(10 ** 8)


class Unionfind:

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
            return 0
        if self.parent[x] < self.parent[y]:
            (x, y) = (y, x)
        total_unite_island = self.parent[x] * self.parent[y]
        self.parent[x] += self.parent[y]
        self.parent[y] = x
        return total_unite_island


(N, M) = map(int, input().split())
A = [0] * M
B = [0] * M
for i in range(M):
    (A[i], B[i]) = map(lambda x: int(x) - 1, input().split())
uf = Unionfind(N)
inconvenience = N * (N - 1) // 2
inconvenience_list = [0] * M
inconvenience_list[M - 1] = inconvenience
for i in range(M - 1, 0, -1):
    inconvenience -= uf.union(A[i], B[i])
    inconvenience_list[i - 1] = inconvenience
for i in range(M):
    print(inconvenience_list[i])
