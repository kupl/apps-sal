n, k = map(int, input().split())
if n == k:
    print("1" * n)
else:
    print((("0" * ((n - k + 2) // 2 - 1) + "1") * (n // ((n - k + 2) // 2) + 1))[:n])
