(n, m) = map(int, input().split())
if n > 2 and m > 2:
    print((n - 2) * (m - 2))
elif n == 1 and m == 1:
    print(1)
elif n == 2 or m == 2:
    print(0)
elif n == 1:
    print(max(m - 2, 0))
elif m == 1:
    print(max(n - 2, 0))
else:
    print(0)
