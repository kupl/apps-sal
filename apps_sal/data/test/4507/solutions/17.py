import sys

dp = []
sum = []
INF = sys.maxsize / 2


def sum_range(a, b):
    if a == 0:
        return sum[b]
    return sum[b] - sum[a - 1]


def rec(pos, sale, n, k):
    if k == 0:
        return 0
    if dp[k] != -1:
        return dp[k]

    res = INF
    for x in range(1, k + 1):
        if sale[x] != -1:
            res = min(res, rec(pos + x, sale, n, k - x) + sum_range(pos + sale[x], pos + x - 1))
    dp[k] = res
    return res


inp = [int(x) for x in sys.stdin.read().split()]

n, m, k = inp[0], inp[1], inp[2]
inp_idx = 3

a = []
for _ in range(n):
    a.append(inp[inp_idx])
    inp_idx += 1

sale = [-1] * (k + 1)
sale[1] = 0
for _ in range(m):
    x, y = inp[inp_idx], inp[inp_idx + 1]
    inp_idx += 2
    if x > k:
        continue
    sale[x] = max(sale[x], y)

a.sort()

sum = [0] * n
sum[0] = a[0]
for i in range(1, n):
    sum[i] = sum[i - 1] + a[i]

dp = [-1] * (k + 1)
cost = rec(0, sale, n, k)
print(cost)
