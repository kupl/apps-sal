import sys

sys.setrecursionlimit(10 ** 5)


def dfs(v):
    if v > 3234566667:
        return
    ans.append(v)
    d = v % 10
    if d - 1 >= 0:
        dfs(v * 10 + d - 1)
    dfs(v * 10 + d)
    if d + 1 < 10:
        dfs(v * 10 + d + 1)


K = int(input())
ans = []
[dfs(i) for i in range(1, 10)]
print((sorted(ans)[K - 1]))
