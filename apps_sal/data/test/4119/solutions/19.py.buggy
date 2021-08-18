n, m = map(int, input().split())
x = list(map(int, input().split()))

if n >= m:
    print('0')
    return

x_sorted = sorted(x)
dx = [abs(x_sorted[i + 1] - x_sorted[i]) for i in range(m - 1)]
dx_sorted = sorted(dx, reverse=True)

result = sum(dx_sorted)
for i in range(n - 1):
    result -= dx_sorted[i]
print(result)
