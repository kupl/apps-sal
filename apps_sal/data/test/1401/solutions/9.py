import sys


def subtree_count():
    stack = [0]
    while len(stack):
        v = stack[-1]

        size = 1
        for u, _ in edge[v]:
            if u in subtree:
                size += subtree[u]
            else:
                stack.append(u)

        if stack[-1] == v:
            stack.pop()
            subtree[v] = size


def remove_bfs():
    queue = [(0, 0)]

    removed = 0

    while len(queue):
        v, s = queue.pop()

        if s > vertex[v]:
            removed += subtree[v]
        else:
            for u, c in edge[v]:
                queue.append((u, max(s + c, 0)))

    return removed

sys.setrecursionlimit(1000001)
n = int(input())

vertex = list(map(int, input().split()))
edge = {}
subtree = {}

for i in range(n):
    edge[i] = []

for i in range(n - 1):
    p, c = list(map(int, input().split()))
    edge[p - 1] += [(i + 1, c)]

subtree_count()
print(remove_bfs())

