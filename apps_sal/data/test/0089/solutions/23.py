n = int(input())

if n % 2 == 0:
    print((n // 2) * (n // 2 + 1))
else:
    nn = (n - 1) // 2
    print(n * (n + 1) // 2 - nn * (nn + 1))
