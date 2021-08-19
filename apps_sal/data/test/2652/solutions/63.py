import copy


class UnionFind:

    def __init__(self, n):
        self.par = [i for i in range(n + 1)]
        self.rank = [0] * (n + 1)

    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
        else:
            self.par[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    def same_check(self, x, y):
        return self.find(x) == self.find(y)


N = int(input())
A = [0] * N
for i in range(N):
    (a, b) = list(map(int, input().split()))
    A[i] = [i, a, b]
B = copy.deepcopy(A)
A = sorted(A, key=lambda x: x[1])
B = sorted(B, key=lambda x: x[2])
A2 = [0] * (N - 1)
for i in range(1, N):
    l = abs(A[i][1] - A[i - 1][1])
    A2[i - 1] = [A[i][0], A[i - 1][0], l]
B2 = [0] * (N - 1)
for i in range(1, N):
    l = abs(B[i][2] - B[i - 1][2])
    B2[i - 1] = [B[i][0], B[i - 1][0], l]
Len = A2 + B2
Len = sorted(Len, key=lambda x: x[2])
data = UnionFind(N + 1)
cost = 0
for i in range(len(Len)):
    if not data.same_check(Len[i][0], Len[i][1]):
        data.union(Len[i][0], Len[i][1])
        cost += Len[i][2]
print(cost)
