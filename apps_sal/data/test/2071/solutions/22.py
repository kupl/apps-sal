R = lambda: map(int, input().split())
n = int(input())
arr = [list(R()), list(R())]
lus = [0] * (n + 1)
lds = [0] * (n + 1)
rs = [0] * (n + 1)
for i in range(n):
    lus[i] = i * arr[0][i] + (2 * n - 1 - i) * arr[1][i]
    lds[i] = i * arr[1][i] + (2 * n - 1 - i) * arr[0][i]
for i in range(n - 1, -1, -1):
    lus[i] += lus[i + 1]
    lds[i] += lds[i + 1]
    rs[i] = rs[i + 1] + arr[0][i] + arr[1][i]
dp = [0] * (n + 1)
for i in range(0, n, 2):
    dp[i] = lus[i] + i * rs[i]
for i in range(1, n, 2):
    dp[i] = lds[i] + i * rs[i]
res = dp[0]
acc = 0
for i in range(n):
    if i % 2 == 0:
        acc += arr[0][i] * (2 * i) + arr[1][i] * (2 * i + 1)
    else:
        acc += arr[1][i] * (2 * i) + arr[0][i] * (2 * i + 1)
    res = max(res, acc + dp[i + 1])
print(res)
