n, m = list(map(int, input().split()))
if n + m == 2:
    print((1))
elif n == 1:
    print((m - 2))
elif m == 1:
    print((n - 2))
elif n == 2 or m == 2:
    print((0))
else:
    print(((n - 2) * (m - 2)))
