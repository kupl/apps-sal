from math import sqrt, floor
n = int(input())
flsq = lambda x: floor(sqrt(x))
clsd = lambda f, x: min(x - f**2, (f + 1)**2 - x)
a = sorted(list([(clsd(flsq(int(s)), int(s)), int(s)) for s in input().split()]))
print(sum(x[0] for x in a[:n // 2]) + sum((1 if a[j][1] != 0 else 2) if a[j][0] == 0 else 0 for j in range(n // 2, n)))
