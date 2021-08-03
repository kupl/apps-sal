n = int(input())
parent = [i for i in range(n)]
kitten = {}


def root(i):
    if parent[i] == i:
        return i
    else:
        parent[i] = root(parent[i])
        return parent[i]


def union(a, b):
    roota = root(a)
    rootb = root(b)
    if roota not in kitten:
        kitten[roota] = [roota]
    if rootb not in kitten:
        kitten[rootb] = [rootb]
    if len(kitten[roota]) >= len(kitten[rootb]):
        parent[rootb] = roota
        kitten[roota] += kitten[rootb]
        del kitten[rootb]
    else:
        parent[roota] = rootb
        kitten[rootb] += kitten[roota]
        del kitten[roota]


for i in range(n - 1):
    x, y = [int(s) - 1 for s in input().split(' ')]
    union(x, y)
print(" ".join([str(i + 1) for i in kitten[root(x)]]))
