h, w, d = list(map(int, input().split()))
n = h*w
paths = [[]for _ in range(d)]
for i in range(n):
    paths[i % d].append(i)


class P:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __sub__(self, p):
        return P(self.x-p.x, self.y-p.y)

    def _abs(self):
        return P(abs(self.x), abs(self.y))

    def _sum(self):
        return self.x+self.y

    def to(self, p):
        return (self-p)._abs()._sum()


coodinates = [None]*n
for i in range(h):
    for j, a in enumerate([int(x)-1 for x in input().split()]):
        coodinates[a] = P(i, j)

costs = [[0]for _ in range(d)]
for i in range(d):
    for x, y in zip(paths[i], paths[i][1:]):
        p, q = coodinates[x], coodinates[y]
        costs[i].append(costs[i][-1]+p.to(q))

q = int(input())
for _ in range(q):
    L, R = [int(x)-1 for x in input().split()]
    print((costs[L % d][R//d]-costs[L % d][L//d]))

