m, b = map(int, input().split())
f = lambda x, y: (x + y) * (x + 1) * (y + 1) >> 1
print(max(f(k * m, b - k) for k in range(b + 1)))
