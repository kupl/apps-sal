class unionFind:
    parent = []

    def __init__(self, N):
        self.parent = [i for i in range(N)]
        self.weight = [0]*N

    def root(self, x):
        if self.parent[x] == x:
            return(x)
        else:
            p = self.root(self.parent[x])
            self.weight[x] += self.weight[self.parent[x]]
            self.parent[x] = p
            return(self.parent[x])

    def same(self, x, y):
        x, y = x-1, y-1
        return(self.root(x) == self.root(y))

    def unite(self, x, y, w):
        w -= self.getWeight(x)
        w += self.getWeight(y)
        x, y = x-1, y-1
        x = self.root(x)
        y = self.root(y)
        if x == y:
            return
        else:
            self.parent[x] = y
            self.weight[x] = self.weight[y]+w
            return

    def getWeight(self, x):
        x -= 1
        self.root(x)
        return(self.weight[x])


def main():
    import sys
    input = sys.stdin.readline

    N, M = list(map(int, input().split()))
    G = unionFind(N)
    for i in range(M):
        L, R, D = list(map(int, input().split()))
        if G.same(L, R):
            x = G.getWeight(L)
            y = G.getWeight(R)
            if x == y + D:
                continue
            else:
                print("No")
                return
        else:
            G.unite(L, R, D)
    print("Yes")


main()

