(n, m) = list(map(int, input().split()))
if n >= 2 and m >= 2:
    print((n - 2) * (m - 2))
elif n == 1 and m == 1:
    print(1)
elif n == 1 and m > 1:
    print(m - 2)
elif n > 1 and m == 1:
    print(n - 2)
