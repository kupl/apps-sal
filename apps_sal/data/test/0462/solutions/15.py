a, b, c = list(map(int, input().split()))
mi = min(a, b, c)
ma = max(a, b, c)
sr = a + b + c - mi - ma
print((ma - sr) + (sr - mi))
