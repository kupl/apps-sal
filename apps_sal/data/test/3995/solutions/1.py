n, k = [int(i) for i in input().split()]
print("1" * n if k == n else (("0" * ((n - k) // 2) + "1") * (n // ((n - k) // 2) + 1))[0:n])

