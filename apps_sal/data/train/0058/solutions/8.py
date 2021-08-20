mem = [[[0 for i in range(51)] for j in range(31)] for k in range(31)]


def f(n, m, k):
    if mem[n][m][k]:
        return mem[n][m][k]
    if n * m == k or k == 0:
        return 0
    cost = 10 ** 9
    for x in range(1, n // 2 + 1):
        for z in range(k + 1):
            cost = min(cost, m * m + f(n - x, m, k - z) + f(x, m, z))
    for y in range(1, m // 2 + 1):
        for z in range(k + 1):
            cost = min(cost, n * n + f(n, m - y, k - z) + f(n, y, z))
    mem[n][m][k] = cost
    return cost


t = int(input())
for i in range(t):
    (n, m, k) = map(int, input().split())
    print(f(n, m, k))
