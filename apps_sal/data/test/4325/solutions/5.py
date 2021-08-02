n, x, t = map(int, input().split())
if n / x == n // x:
    print(n // x * t)
else:
    print((n // x + 1) * t)
