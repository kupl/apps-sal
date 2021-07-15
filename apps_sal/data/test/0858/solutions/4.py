n = int(input())
if (n % 2 == 1):
    print(n // 2)
else:
    x = 1
    while (x <= n):
        x *= 2
    print((n - x // 2) // 2)


