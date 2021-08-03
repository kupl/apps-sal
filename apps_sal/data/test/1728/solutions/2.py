import sys
sys.setrecursionlimit(1000000)
read = sys.stdin.readline

n = int(read())
parent = [1] + list(map(int, read().split()))
color = list(map(int, read().split()))
underVertex = [[] for _ in range(n + 1)]

for i, p in enumerate(parent):
    if i + 1 != p:
        underVertex[p] += [i + 1]


def dfs(idx, c):
    count = 0
    if c != color[idx - 1]:
        count = 1
    for nxt in underVertex[idx]:
        count += dfs(nxt, color[idx - 1])
    return count


print(dfs(1, 0))
