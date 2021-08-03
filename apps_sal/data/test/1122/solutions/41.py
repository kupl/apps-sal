n, m = map(int, input().split())

if n % 2 != 0:
    for i in range(m):
        print(1 + i, n - i)
else:
    for i in range(m):
        if (n - i) - (1 + i) > n / 2:
            print(1 + i, n - i)
        else:
            print(1 + i, n - i - 1)
