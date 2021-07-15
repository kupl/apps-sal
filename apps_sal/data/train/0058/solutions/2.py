d = [[[0 for i in range(51)] for j in range(31)] for k in range(31)]


def rec(n, m, k):
    nonlocal d
    if n*m == k or k == 0:
        return 0
    if d[n][m][k] > 0:
        return d[n][m][k]
    if n*m<k:
        return 10**10
    cost = 10**10
    for i in range(1, n // 2 + 1):
        for j in range(k+1):
            cost = min(cost, m*m + rec(n-i, m, k-j) + rec(i, m, j))
    for i in range(1, m // 2 + 1):
        for j in range(k+1):
            cost = min(cost, n*n + rec(n, m-i, k-j) + rec(n, i, j))
    d[n][m][k] = cost
    return cost

p = []
t = int(input())
for i in range(t):
    n, m, k = list(map(int, input().split()))
    p.append(rec(n, m, k))
print('\n'.join(str(x) for x in p))

