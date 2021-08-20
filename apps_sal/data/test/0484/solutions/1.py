import sys
(n, a, b) = list(map(int, input().split()))
x = []
y = []
for i in range(n):
    (x1, y1) = list(map(int, input().split()))
    x.append(x1)
    y.append(y1)
ans = 0
for i in range(n):
    for j in range(i + 1, n):
        s = x[i] * y[i] + x[j] * y[j]
        if x[i] + x[j] <= a and max(y[i], y[j]) <= b:
            ans = max(ans, s)
        if x[i] + x[j] <= b and max(y[i], y[j]) <= a:
            ans = max(ans, s)
        if x[i] + y[j] <= a and max(y[i], x[j]) <= b:
            ans = max(ans, s)
        if x[i] + y[j] <= b and max(y[i], x[j]) <= a:
            ans = max(ans, s)
        if y[i] + y[j] <= a and max(x[i], x[j]) <= b:
            ans = max(ans, s)
        if y[i] + y[j] <= b and max(x[i], x[j]) <= a:
            ans = max(ans, s)
        if y[i] + x[j] <= a and max(x[i], y[j]) <= b:
            ans = max(ans, s)
        if y[i] + x[j] <= b and max(x[i], y[j]) <= a:
            ans = max(ans, s)
print(ans)
