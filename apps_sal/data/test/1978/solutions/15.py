from collections import deque
n = int(input())
graph = [list([bit == '1' for bit in list(input())]) for _ in range(n)]
m = int(input())
way = list([int(i) - 1 for i in input().split()])
# print(graph)


def dfs(start):
    queue = deque([start])
    d = [-1] * n
    d[start] = 0
    while len(queue) != 0:
        u = queue[0]
        queue.popleft()
        for v in range(n):
            if graph[u][v] and d[v] == -1:
                d[v] = d[u] + 1
                queue.append(v)
    return d


minpath = list(map(dfs, list(range(n))))
good = [way[0]]
checkp = way[0]
for i in range(1, m):
    prev = way[i - 1]
    if minpath[checkp][way[i]] != minpath[checkp][prev] + 1:
        good.append(prev)
        checkp = prev
# print(minpath)
good.append(way[-1])
print(len(good))
print(' '.join([str(p + 1) for p in good]))
