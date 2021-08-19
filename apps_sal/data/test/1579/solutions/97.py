import sys
sys.setrecursionlimit(10 ** 5)
v = 100005
visited = [False] * (2 * v)
count = [0, 0]


def dfs(a):
    visited[a] = True
    count[a // v] += 1
    for i in vertex[a]:
        if not visited[i]:
            dfs(i)


input = sys.stdin.readline
N = int(input())
vertex = [[] for _ in range(v * 2)]
for _ in range(N):
    (x, y) = map(int, input().split())
    y += v
    vertex[x].append(y)
    vertex[y].append(x)
ans = 0
for i in range(v):
    if not visited[i]:
        count = [0, 0]
        dfs(i)
        ans += count[0] * count[1]
print(ans - N)
