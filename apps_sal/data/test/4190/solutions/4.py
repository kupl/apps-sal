class MinArray:

    def __init__(self, n, a, b):
        self.n = n
        self.a = a
        self.b = b
        self.cnts = [0] * self.n
        self.par = [i for i in range(self.n)]
        self.size = [1] * self.n
        for v in self.b:
            self.cnts[v] += 1

    def find(self, v):
        while v != self.par[v]:
            tmp = self.par[v]
            self.par[v] = self.par[tmp]
            v = tmp
        return v

    def union(self, u, v):
        (u, v) = (self.find(u), self.find(v))
        self.par[u] = v

    def build_tree(self):
        for i in range(self.n - 1, -1, -1):
            if self.cnts[i] == 0:
                self.union(i, (i + 1) % self.n)

    def get_min(self):
        self.build_tree()
        arr = []
        for u in self.a:
            v = self.find((self.n - u) % self.n)
            arr.append((u + v) % self.n)
            self.cnts[v] -= 1
            if self.cnts[v] == 0:
                self.union(v, (v + 1) % self.n)
        print(*arr)


n = int(input())
a = list(map(int, input().strip(' ').split(' ')))
b = list(map(int, input().strip(' ').split(' ')))
ma = MinArray(n, a, b)
ma.get_min()
