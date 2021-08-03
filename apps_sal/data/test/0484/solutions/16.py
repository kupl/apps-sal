n, a, b = list(map(int, input().split()))
x = list(range(n))
y = list(range(n))
for i in range(n):
    x[i], y[i] = list(map(int, input().split()))
ans = 0
for i in range(n):
    for j in range(i + 1, n):
        # 4 ways of rotating
        if (x[i] + x[j] <= b and max(y[i], y[j]) <= a) or (y[i] + y[j] <= a and max(x[i], x[j]) <= b):
            ans = max(ans, x[i] * y[i] + x[j] * y[j])
        x[i], y[i] = y[i], x[i]
        if (x[i] + x[j] <= b and max(y[i], y[j]) <= a) or (y[i] + y[j] <= a and max(x[i], x[j]) <= b):
            ans = max(ans, x[i] * y[i] + x[j] * y[j])
        x[j], y[j] = y[j], x[j]
        if (x[i] + x[j] <= b and max(y[i], y[j]) <= a) or (y[i] + y[j] <= a and max(x[i], x[j]) <= b):
            ans = max(ans, x[i] * y[i] + x[j] * y[j])
        x[i], y[i] = y[i], x[i]
        if (x[i] + x[j] <= b and max(y[i], y[j]) <= a) or (y[i] + y[j] <= a and max(x[i], x[j]) <= b):
            ans = max(ans, x[i] * y[i] + x[j] * y[j])
        x[j], y[j] = y[j], x[j]
print(ans)
