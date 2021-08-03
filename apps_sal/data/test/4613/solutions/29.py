n, m = map(int, input().split())
reach = [0] * (n + 1)
l = [[] for i in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    l[a].append(b)
    l[b].append(a)


def dfs(s, parent):
    reach[s] = 1
    for i in l[s]:
        if i == parent:
            continue
        if reach[i] == 0:
            dfs(i, s)
        else:
            reach[i] += 1


loop = [0] * (n + 1)
for i in range(1, n + 1):
    reach = [0] * (n + 1)
    dfs(i, 0)
    if reach[i] != 1:
        loop[i] = 1
ans = 0
for i in range(1, n + 1):
    for j in l[i]:
        if loop[i] == 1 and loop[j] == 1:
            ans += 1
print(m - ans // 2)
