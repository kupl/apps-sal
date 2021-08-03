# coding=utf-8

n, m = list(map(int, input().split()))
a = [[] for _ in range(n + 1)]
for i in range(m):
    a1, a2 = list(map(int, input().split()))
    a[a2].append(a1)
    a[a1].append(a2)
ans, f, flag = 0, [0] * (n + 1), 1


def dfs(x):
    f[x] = 1
    mid = []
    mid.append(x)
    while mid:
        v = mid.pop()
        if len(a[v]) != 2:
            nonlocal flag
            flag = 0
        for i in a[v]:
            if not f[i]:
                f[i] = 1
                mid.append(i)


for i in range(1, n + 1):
    if not f[i]:
        flag = 1
        dfs(i)
        ans += flag
print(ans)
