import sys
sys.setrecursionlimit(10 ** 8)


def dfs(v, c):
    now = 1
    for (u, i) in edge[v]:
        if color[i] == 0:
            if now == c:
                now += 1
            color[i] = now
            dfs(u, now)
            now += 1
    return 0


N = int(input())
edge = [[] for _ in range(N)]
for i in range(N - 1):
    (a, b) = map(int, input().split())
    edge[a - 1].append([b - 1, i])
    edge[b - 1].append([a - 1, i])
color = [0] * (N - 1)
dfs(0, 1 << 30)
print(max(color))
print(*color, sep='\n')
