n, m, a, b = list(map(int, input().split()))
if n % m == 0:
    print(0)
else:
    res1 = (n % m) * b
    res2 = (m - n % m) * a
    print(min(res1, res2))
