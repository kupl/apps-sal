import heapq

class BalancingTree:
    def __init__(self):
        self.p = []
        self.q = []

    def insert(self, x):
        heapq.heappush(self.p, x)

    def erase(self, x):
        heapq.heappush(self.q, x)

    def minimum(self):
        while self.q and self.p[0] == self.q[0]:
            heapq.heappop(self.p)
            heapq.heappop(self.q)
        return self.p[0] if self.p else None


MAX = 2*10**5
n, q = list(map(int, input().split()))
ab = []
k = [BalancingTree() for _ in range(MAX)]
for i in range(n):
    a, b = list(map(int, input().split()))
    b -= 1
    ab.append([a, b])
    k[b].insert(-a)

k_max = BalancingTree()
for i in range(MAX):
    if v := k[i].minimum():
        k_max.insert(-v)

for _ in range(q):
    c, d = [int(x)-1 for x in input().split()]
    a, b = ab[c]
    k_max.erase(-k[b].minimum())
    if v := k[d].minimum():
        k_max.erase(-v)
    k[b].erase(-a)

    k[d].insert(-a)
    if v := k[b].minimum():
        k_max.insert(-v)
    k_max.insert(-k[d].minimum())
    ab[c][1] = d

    print((k_max.minimum()))

