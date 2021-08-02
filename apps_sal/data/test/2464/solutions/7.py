import sys


class UnionFind():

    def __init__(self, n):
        self.n = n

        self.root = [-1] * (n + 1)

        self.rnk = [0] * (n + 1)

    def Find_Root(self, x):
        if(self.root[x] < 0):
            return x
        else:

            self.root[x] = self.Find_Root(self.root[x])
            return self.root[x]

    def Unite(self, x, y):

        x = self.Find_Root(x)
        y = self.Find_Root(y)

        if(x == y):
            return

        elif(self.rnk[x] > self.rnk[y]):
            self.root[x] += self.root[y]
            self.root[y] = x

        else:
            self.root[y] += self.root[x]
            self.root[x] = y

            if(self.rnk[x] == self.rnk[y]):
                self.rnk[y] += 1

    def isSameGroup(self, x, y):
        return self.Find_Root(x) == self.Find_Root(y)

    def Count(self, x):
        return -self.root[self.Find_Root(x)]


input = sys.stdin.readline

N = int(input())
uni0 = UnionFind(N)
uni1 = UnionFind(N)
for _ in range(N - 1):
    a, b, c = map(int, input().split())
    if c == 0:
        uni0.Unite(a - 1, b - 1)
    else:
        uni1.Unite(a - 1, b - 1)

g0 = {}
g1 = {}
for i in range(N):
    if uni0.Count(i) != 1:
        r = uni0.Find_Root(i)
        if not r in g0.keys():
            g0[r] = [i]
        else:
            g0[r].append(i)
    if uni1.Count(i) != 1:
        r = uni1.Find_Root(i)
        if not r in g1.keys():
            g1[r] = [i]
        else:
            g1[r].append(i)

ans = 0
for v_list in g1.values():
    c = 0
    for n in v_list:
        if uni0.Count(n) == 1:
            c += 1
    l = len(v_list)
    ans += c * (l - 1)

for v_list in g0.values():
    c = 0
    for n in v_list:
        if uni1.Count(n) != 1:
            r = uni1.Find_Root(n)
            c += len(g1[r]) - 1
    c += len(v_list) - 1
    ans += len(v_list) * c

print(ans)
