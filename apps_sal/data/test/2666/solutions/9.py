n, k = map(int, input().split())
k = k // 2
l = []
for _ in range(n):
    l.append(int(input()))


def fip(p, no, kt):
    pr = [[0 for i in range(n + 1)] for j in range(k + 1)]

    for i in range(1, k + 1):
        pd = float('-inf')

        for j in range(1, n):

            pd = max(pd, pr[i - 1][j - 1] - p[j - 1])

            pr[i][j] = max(pr[i][j - 1], p[j] + pd)

    return pr[k][n - 1]


print(fip(l, n, k))
