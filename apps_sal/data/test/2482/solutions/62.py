class UnionFind():
    def __init__(self, n):
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x


def main():
    import sys
    from collections import Counter
    # readline = sys.stdin.readline
    readlines = sys.stdin.readlines
    N, K, L = list(map(int, input().split()))
    uf1 = UnionFind(N)
    uf2 = UnionFind(N)

    IN = readlines()
    for i in range(K):
        p, q = list(map(int, IN[i].split()))
        p -= 1; q -= 1
        uf1.union(p, q)
    for j in range(K, K + L):
        r, s = list(map(int, IN[j].split()))
        r -= 1; s -= 1
        # if uf1.find(r) == uf1.find(s):
        uf2.union(r, s)
    
    # ans = []
    # for i in range(N):
    #     ans.append(-uf2.parents[uf2.find(i)])
    # print(*ans)
    path = []
    C = Counter()
    for i in range(N):
        pair = (uf1.find(i), uf2.find(i))
        path.append(pair)
        C[pair] += 1

    ans = []
    for i in range(N):
        ans.append(C[path[i]])
    print((*ans))


def __starting_point():
    main()

__starting_point()
