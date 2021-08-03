class Union():
    def __init__(self, n):
        self.para = [-1] * n

    def find(self, n):
        if self.para[n] < 0:
            return n

        else:
            self.para[n] = self.find(self.para[n])
            return self.para[n]

    def union(self, n, m):
        n = self.find(n)
        m = self.find(m)
        if n == m:
            return False
        else:
            if self.para[n] > self.para[m]:
                n, m = m, n

            self.para[n] += self.para[m]
            self.para[m] = n

    def same(self, n, m):
        return self.find(n) == self.find(m)


N = int(input())
X, Y = [], []
for i in range(N):
    x, y = map(int, input().split())
    X.append((x, i))
    Y.append((y, i))
X.sort()
Y.sort()
ALL = []
for i in range(len(X) - 1):
    ALL.append((X[i + 1][0] - X[i][0], X[i][1], X[i + 1][1]))
    ALL.append((Y[i + 1][0] - Y[i][0], Y[i][1], Y[i + 1][1]))
ALL.sort()
ut = Union(N)
cnt = 0
for a in ALL:
    n = a[1]
    m = a[2]
    if not ut.same(n, m):
        ut.union(n, m)
        cnt += a[0]
print(cnt)
