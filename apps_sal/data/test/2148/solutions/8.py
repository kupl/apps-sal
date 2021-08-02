read = lambda: list(map(int, input().split()))
n, r = read()
x = list(read())
y = [0] * n
for i in range(n):
    cur = r
    for j in range(i):
        if 2 * r >= abs(x[i] - x[j]):
            cur = max(cur, y[j] + ((4 * r * r - (x[i] - x[j]) ** 2) ** 0.5))
    y[i] = cur
print(*y)
