ss = list(map(lambda c: c in 'IEAOUY', input()))
n = len(ss)
w = [0] * n
for i in range(1, n + 1):
    w[0] += 1 / i
w[n - 1] = w[0]
sigma = w[0]
for i in range(1, (n - 1) // 2 + 1):
    sigma -= 1 / i + 1 / (n + 1 - i)
    w[n - i - 1] = w[i] = w[i - 1] + sigma
ans = 0
for i in range(0, n):
    ans += ss[i] * w[i]
print(ans)
