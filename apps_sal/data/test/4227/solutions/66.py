def dfs(x, l):
    if l.count(False) == 0:
        return 1
    cnt = 0
    for i in a[x]:
        if not l[i]:
            cnt += dfs(i, [[True] if j == i else l[j] for j in range(n)])
    return cnt


(n, m) = map(int, input().split())
a = [[] for i in range(n)]
for i in range(m):
    x = list(map(int, input().split()))
    a[x[0] - 1].append(x[1] - 1)
    a[x[1] - 1].append(x[0] - 1)
print(dfs(0, [True] + [False] * (n - 1)))
