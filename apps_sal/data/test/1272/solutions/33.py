class UnionFind:

    def __init__(self, n):
        self.n = n
        self.root = [-1] * (n + 1)
        self.rnk = [0] * (n + 1)

    def Find_Root(self, x):
        if self.root[x] < 0:
            return x
        else:
            self.root[x] = self.Find_Root(self.root[x])
            return self.root[x]

    def Unite(self, x, y):
        x = self.Find_Root(x)
        y = self.Find_Root(y)
        if x == y:
            return
        elif self.rnk[x] > self.rnk[y]:
            self.root[x] += self.root[y]
            self.root[y] = x
        else:
            self.root[y] += self.root[x]
            self.root[x] = y
            if self.rnk[x] == self.rnk[y]:
                self.rnk[y] += 1

    def isSameGroup(self, x, y):
        return self.Find_Root(x) == self.Find_Root(y)

    def Count(self, x):
        ret = -self.root[self.Find_Root(x)]
        return ret


(N, M) = map(int, input().split())
A = [0] * M
B = [0] * M
for i in range(M):
    (A[i], B[i]) = map(int, input().split())
conv = N * (N - 1) // 2
UN = UnionFind(N)
ans = [conv]
for j in range(M - 1, 0, -1):
    if UN.isSameGroup(A[j], B[j]):
        pass
    else:
        conv -= UN.Count(A[j]) * UN.Count(B[j])
    ans.append(conv)
    UN.Unite(A[j], B[j])
for p in ans[::-1]:
    print(p)
