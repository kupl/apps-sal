(n, m) = map(int, input().split())
if n >= 2 and m >= 2:
    print((n - 2) * (m - 2))
if n >= 2 and m == 1:
    print(n - 2)
if n == 1 and m >= 2:
    print(m - 2)
if n == 1 and m == 1:
    print(1)
