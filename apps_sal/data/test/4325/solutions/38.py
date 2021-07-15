n, x, t = list(map(int, input().split()))

if n / x == int(n / x):
    print((((n // x)) * t))
else:
    print((((n // x) + 1) * t))

