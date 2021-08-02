n, k = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(abs, x))
ans = float("inf")

for i in range(n - k + 1):
    if 0 < x[i] * x[i + k - 1]:
        cost = max(y[i], y[i + k - 1])

    else:
        cost = y[i] + y[i + k - 1] + min(-x[i], x[i + k - 1])

    ans = min(ans, cost)

print(ans)
