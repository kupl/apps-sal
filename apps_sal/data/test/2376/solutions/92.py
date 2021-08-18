N, W = list(map(int, input().split()))
wv = []

for _ in range(N):
    wv.append(tuple(map(int, input().split())))


memo = {}


def dfs(i, j):
    if (i, j) in memo:
        return memo[(i, j)]

    if i < 0 or j <= 0:
        return 0

    ret = 0
    wi, vi = wv[i]
    if j - wi < 0:
        ret = dfs(i - 1, j)
    else:
        ret = max(dfs(i - 1, j), dfs(i - 1, j - wi) + vi)

    memo[(i, j)] = ret

    return ret


print((dfs(N - 1, W)))
