(n, m, a, b) = list(map(int, input().split()))
if n % m == 0:
    print(0)
else:
    print(min(n % m * b, (m - n % m) * a))
