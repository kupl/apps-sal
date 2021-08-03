from collections import deque


def dfs(n):
    """
    Traverse graph using DFS
    @return: minimum gold value of connected group
    """
    nonlocal visited
    minimum = -1
    queue = deque([n])
    while queue:
        node = queue.popleft()
        visited[node] = True
        if minimum == -1:
            minimum = gold[node]
        else:
            minimum = min(minimum, gold[node])
        for neighbor in adj_list[node]:
            if not visited[neighbor - 1]:
                queue.append(neighbor - 1)
    return minimum


n, m = list(map(int, input().split()))
gold = list(map(int, input().split()))
adj_list = [list() for _ in range(n)]
for _ in range(m):
    x, y = list(map(int, input().split()))
    adj_list[x - 1].append(y)
    adj_list[y - 1].append(x)
visited = [False for _ in range(n)]
total = 0
for i in range(n):
    if not visited[i]:
        total += dfs(i)
print(total)
