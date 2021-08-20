import sys


class Node:

    def __init__(self, val):
        self.parent = self
        self.size = 1


def union(x, y):
    (xRoot, yRoot) = (find(x), find(y))
    if xRoot == yRoot:
        return
    if xRoot.size >= yRoot.size:
        yRoot.parent = xRoot
        xRoot.size += yRoot.size
    else:
        xRoot.parent = yRoot
        yRoot.size += xRoot.size


def find(x):
    while x.parent != x:
        x = x.parent
    return x


(n, m) = [int(item) for item in sys.stdin.readline().strip().split()]
node = [Node(x) for x in range(n + 1)]
groups = [[int(item) for item in sys.stdin.readline().strip().split()] for _ in range(m)]
for g in range(m):
    group = groups[g]
    k = group[0]
    if k == 0:
        continue
    for i in range(2, k + 1):
        union(node[group[i]], node[group[i - 1]])
ans = [find(node[x]).size for x in range(1, n + 1)]
sys.stdout.write(' '.join((str(x) for x in ans)) + '\n')
