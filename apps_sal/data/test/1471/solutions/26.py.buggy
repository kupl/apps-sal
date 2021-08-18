import sys
sys.setrecursionlimit(10**6)
n = int(input())
path = [[] for i in range(n)]
for i in range(n - 1):
    u, v, w = map(int, input().split())
    path[u - 1].append((v - 1, w % 2))
    path[v - 1].append((u - 1, w % 2))
ans = [0] + [-1] * (n - 1)


def dfs(i):
    nonlocal n, path, ans
    for j in path[i]:
        if ans[j[0]] == -1:
            if j[1]:
                ans[j[0]] = 1 - ans[i]
                dfs(j[0])
            else:
                ans[j[0]] = ans[i]
                dfs(j[0])


dfs(0)
print("\n".join(map(str, ans)))
