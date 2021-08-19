(n, m) = map(int, input().split())
if n == 1 or m == 1:
    print(0)
else:
    print((n - 1) * (m - 1))
