import sys
input = sys.stdin.readline
n = int(input())
abd = [list(map(int, input().split())) for i in range(n - 1)]
graph = [[] for i in range(n + 1)]
deg = [0] * (n + 1)
if n == 2:
    print(2)
    return
for a, b, d in abd:
    graph[a].append((b, d))
    graph[b].append((a, d))
    deg[a] += 1
    deg[b] += 1
dp = [[0] * 3 for i in range(n + 1)]
stack = []
root = 0
for i in range(1, n + 1):
    if deg[i] == 1:
        stack.append(i)
    elif not root:
        root = i
        deg[root] += 1
while stack:
    x = stack.pop()
    if dp[x][0] == dp[x][1] == 0:
        for y, d in graph[x]:
            dp[y][d] += 1
            deg[y] -= 1
            if deg[y] == 1:
                stack.append(y)
    else:
        for y, d in graph[x]:
            if deg[y] > 1:
                dp[y][d] += dp[x][d] + 1
                if d == 1:
                    dp[y][2] += dp[x][0] + dp[x][2]
                deg[y] -= 1
                if deg[y] == 1:
                    stack.append(y)
stack = [root]
deg[root] -= 1
while stack:
    x = stack.pop()
    for y, d in graph[x]:
        if deg[y] == 1:
            deg[y] -= 1
            dp[y][d] += dp[x][d] - dp[y][d]
            if d == 1:
                dp[y][2] += dp[x][2] + dp[x][0] - dp[y][0] - dp[y][2]
            stack.append(y)
ans = 0
for i, j, k in dp:
    ans += i + j + k
print(ans)
