

class UnionFind(object):
    def __init__(self, n):
        self.root = [i for i in range(n)]
        self.size = [1 for _ in range(n)]

    def find(self, x):
        if self.root[x] == x:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        x, y = self.find(x), self.find(y)
        if x == y:
            return
        if self.size[x] < self.size[y]:
            x, y = y, x
        self.root[y] = x
        self.size[x] += self.size[y]


def pow_mod(a, b, p):
    ret = 1
    while b > 0:
        if b % 2 == 1:
            ret = ret * a % p
        b //= 2
        a = a * a % p
    return ret


def main():
    n, k = list(map(int, input().split()))

    union_find = UnionFind(n + 1)
    for _ in range(n - 1):
        u, v, c = list(map(int, input().split()))
        if c == 0:
            union_find.union(u, v)

    p = int(1e9 + 7)
    ret = pow_mod(n, k, p)
    used = set()
    for i in range(1, n + 1):
        x = union_find.find(i)
        if x not in used:
            ret = (ret + p - pow_mod(union_find.size[x], k, p)) % p
            used.add(x)
    print(ret)


def __starting_point():
    main()


__starting_point()
