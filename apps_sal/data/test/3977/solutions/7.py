class Union:

    def __init__(self, n):
        self.ancestors = [i for i in range(n+1)]
        self.size = [0]*(n+1)

    def get_root(self, node):
        if self.ancestors[node] == node:
            return node
        self.ancestors[node] = self.get_root(self.ancestors[node])
        return self.ancestors[node]

    def merge(self, a, b):
        a, b = self.get_root(a), self.get_root(b)
        self.ancestors[a] = b


def combination(number):
    return (number * (number - 1)) >> 1


n, m, k = map(int, input().split())
biggest, others, res = 0, n, -m
homes = list(map(int, input().split()))
union = Union(n)

for _ in range(m):
    a, b = map(int, input().split())
    union.merge(a, b)

for i in range(1, n+1):
    union.size[union.get_root(i)] += 1

for home in homes:
    size = union.size[union.get_root(home)]
    biggest = max(biggest, size)
    res += combination(size)
    others -= size

res -= combination(biggest)
res += combination(biggest + others)
print(res)
