import sys
sys.setrecursionlimit(10**5)
n = int(input())
ab = [list(map(int, input().split()))for _ in range(n - 1)]

graph = [[] for _ in range(n + 1)]
ans = [0] * (n - 1)
for i in range(n - 1):
    graph[ab[i][0]].append((ab[i][1], i))
    graph[ab[i][1]].append((ab[i][0], i))

visit = [False] * (n + 1)


def dfs(p, c):
    color = 1
    visit[p] = True
    for n, i in graph[p]:
        if visit[n] == False:
            if color == c:
                color += 1
            ans[i] = color
            dfs(n, color)
            color += 1


dfs(1, 0)
print((max(ans)))
for t in ans:
    print(t)
