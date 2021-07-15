import sys

sys.setrecursionlimit(200000)

n, m = list(map(int, input().split()))

graph = [[] for _ in range(n)]
notused = [True for _ in range(n)]

for _ in range(m):
    x, y = list(map(int, input().split()))
    x -= 1
    y -= 1
    graph[x].append(y)
    graph[y].append(x)

def dfs(x, pre):
    if notused[x]:
        notused[x] = False
        res = True
        for i in graph[x]:
            if pre != i:
                res = res and dfs(i, x)
        return res
    else:
        return False

k = 0
for j in range(n):
    if notused[j]:
        if dfs(j, -1):
            k += 1

print(k)

