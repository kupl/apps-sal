import sys
import math
sys.setrecursionlimit(10 ** 8)


def ini():
    return int(sys.stdin.readline())


def inm():
    return map(int, sys.stdin.readline().split())


def inl():
    return list(inm())


def ins():
    return sys.stdin.readline().rstrip()


debug = lambda *a, **kw: print('\x1b[33m', *a, '\x1b[0m', **dict(file=sys.stderr, **kw))


class Node:

    def __init__(self):
        self.edge = []
        self.count = 0


def dfs(tree, node, p_node, p_count, counts):
    count = tree[node].count + p_count
    counts[node] = count
    for x in tree[node].edge:
        if x == p_node:
            continue
        dfs(tree, x, node, count, counts)


(N, Q) = inm()
tree = []
for _ in range(N):
    tree.append(Node())
for _ in range(N - 1):
    (a, b) = inm()
    tree[a - 1].edge.append(b - 1)
    tree[b - 1].edge.append(a - 1)
for _ in range(Q):
    (p, x) = inm()
    tree[p - 1].count += x
val = []
for _ in range(N):
    val.append(0)
dfs(tree, 0, -1, 0, val)
counts_str = [str(n) for n in val]
s = ' '.join(counts_str)
print(s)
