import sys
sys.setrecursionlimit(10 ** 7)
(n, q) = map(int, input().split())
ans = [0 for _ in range(n)]
gra = [[] for _ in range(n)]
visited = [0 for _ in range(n)]
for _ in range(n - 1):
    (a, b) = map(int, input().split())
    gra[a - 1].append(b - 1)
    gra[b - 1].append(a - 1)
for _ in range(q):
    (p, x) = map(int, input().split())
    ans[p - 1] += x


def dfs(st):
    temp = gra[st]
    for i in temp:
        if visited[i] == 0:
            visited[i] += 1
            ans[i] += ans[st]
            dfs(i)


visited[0] += 1
dfs(0)
for h in range(n):
    ans[h] = str(ans[h])
print(' '.join(ans))
