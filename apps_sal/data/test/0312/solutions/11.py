(n, m) = list(map(int, input().split(' ')))
if n == 1:
    print(1)
elif n % 2 == 0:
    if m <= n // 2:
        print(m + 1)
    else:
        print(m - 1)
elif m <= (n - 1) // 2:
    print(m + 1)
else:
    print(m - 1)
