n, k = [int(i) for i in input().split()]
print((("0" * ((n - k) // 2) + "1") * (n // ((n - k) // 2 + 1) + 1))[:n])
