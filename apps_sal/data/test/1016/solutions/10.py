def dfs(i):
    used[i] = True;
    for j in graph[i]:
        if not used[j]:
            dfs(j)

n, m = list(map(int, input().split()))
graph = [[] for i in range(n)]
for i in range(m):
    a, b = list(map(int, input().split()))
    a -= 1;
    b -= 1;
    graph[a] += [b]
    graph[b] += [a]
used = [False for i in range(n)]
cc = 0
for i in range(n):
    if not used[i]:
        cc += 1;
        dfs(i)
print(1 << (n - cc))

