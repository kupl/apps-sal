n, m = map(int, input().split())

if n == 1 and m == 1:
    print(1)
elif n == 1 or m == 1:
    print(max(n, m) - 2)
elif n >= 3 and m >= 3:
    print((n - 2) * (m - 2))
else:
    print(0)
