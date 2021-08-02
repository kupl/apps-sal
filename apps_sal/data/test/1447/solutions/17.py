n, m = map(float, input().split())
if n == 1: print(1)
else: print((1 + (n - 1) * (m - 1) / (n * m - 1)) / n)
