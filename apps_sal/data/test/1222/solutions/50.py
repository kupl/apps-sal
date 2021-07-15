import sys

sys.setrecursionlimit(10 ** 5)


def dfs(v):
    ans.append(v)
    if v > 1_000_000_000:
        return
    for d in range(10):
        if abs(d - v % 10) <= 1:
            nv = v * 10 + d
            dfs(nv)


K = int(input())
ans = []
[dfs(i) for i in range(1, 10)]
print((sorted(ans)[K - 1]))

