class UnionFind:
    def __init__(self, n):
        self.n = n
        self.g = [i for i in range(n)]
        self.nmembers = [1 for i in range(n)]

    def __len__(self):
        return self.n

    def __str__(self):
        return "group:{}\nnmembers:{}".format(self.g, self.nmembers)

    def __getitem__(self, x):
        return self.whichgroup(x)

    def merge(self, x, y):
        gx = self.whichgroup(x)
        gy = self.whichgroup(y)
        if gx != gy:
            nx = self.nmembers[gx]
            ny = self.nmembers[gy]
            ming = min(gx, gy)
            maxg = gx + gy - ming
            self.g[maxg] = ming
            self.nmembers[maxg] = 0
            self.nmembers[ming] = nx + ny

    def whichgroup(self, x):
        if x != self.g[x]:
            self.g[x] = self.whichgroup(self.g[x])
            self.nmembers[x] = 0
            return self.g[x]
        else:
            return x


N, M, K = list(map(int, input().split()))
UF = UnionFind(N)
F = [0 for i in range(N)]
B = [0 for i in range(N)]
for i in range(M):
    x, y = list(map(int, input().split()))
    x, y = x - 1, y - 1
    UF.merge(x, y)
    F[x] += 1
    F[y] += 1
for i in range(K):
    x, y = list(map(int, input().split()))
    x, y = x - 1, y - 1

    gx = UF.whichgroup(x)
    gy = UF.whichgroup(y)
    if gx == gy:
        B[x] += 1
        B[y] += 1
ans = []
for i in range(N):
    ans.append(UF.nmembers[UF[i]] - B[i] - F[i] - 1)
print((*ans))
