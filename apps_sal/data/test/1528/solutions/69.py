N, X = list(map(int, input().split(' ')))

level2p = [1] * (N + 1)
level2pb = [1] * (N + 1)

for i in range(N):
    level2p[i + 1] = level2p[i] * 2 + 1
    level2pb[i + 1] = level2pb[i] * 2 + 3


def dfs(n, x):
    if n == 0:
        return 1

    if x <= 1:
        return 0
    elif x <= 1 + level2pb[n - 1]:
        return dfs(n - 1, x - 1)
    elif x <= 1 + level2pb[n - 1] + 1:
        return level2p[n - 1] + 1
    elif x <= 1 + level2pb[n - 1] + 1 + level2pb[n - 1]:
        return level2p[n - 1] + 1 + dfs(n - 1, x - 1 - level2pb[n - 1] - 1)
    else:
        return level2p[n]


print((dfs(N, X)))

