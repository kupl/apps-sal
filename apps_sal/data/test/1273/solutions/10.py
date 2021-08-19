import sys
sys.setrecursionlimit(10 ** 6)
n = int(input())
t = [[] for _ in range(n + 1)]
for i in range(n - 1):
    (a, b) = map(int, input().split())
    t[a].append((b, i))
    t[b].append((a, i))
num = max([len(tmp) for tmp in t])
print(num)
ans = [-1] * (n - 1)


def dfs(n, before, bcol):
    col = 1
    for (i, j) in t[n]:
        if i == before:
            continue
        if col == bcol:
            col += 1
        ans[j] = col
        dfs(i, n, col)
        col += 1


dfs(1, 0, -1)
for i in range(n - 1):
    print(ans[i])
