def check(l):
    nonlocal a, b, s, ans
    if min(l) <= min(a, b) and max(l) <= max(a, b):
        ans = max(ans, s)


ans = 0
x = []
y = []
n, a, b = list(map(int, input().split()))
for _ in range(n):
    xi, yi = list(map(int, input().split()))
    x.append(xi)
    y.append(yi)

ans = 0
for i in range(n - 1):
    for j in range(i + 1, n):
        s = x[i] * y[i] + x[j] * y[j]
        check([max(x[i], x[j]), y[i] + y[j]])
        check([max(x[i], y[j]), y[i] + x[j]])
        check([max(y[i], x[j]), x[i] + y[j]])
        check([max(y[i], y[j]), x[i] + x[j]])
        check([x[i] + x[j], y[i] + y[j]])
        check([x[i] + y[j], y[i] + x[j]])

print(ans)

