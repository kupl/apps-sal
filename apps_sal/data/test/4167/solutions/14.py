n, k = map(int, input().split())

if k % 2 == 1:
    print((n // k) ** 3)
else:
    print((((n + k // 2) // k)**3) + ((n // k)**3))
