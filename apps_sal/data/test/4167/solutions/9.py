n, k = list(map(int, input().split()))
if k % 2 == 1:
    print((int(n // k)**3))
else:
    s = k // 2
    print((int((n + s) // (2 * s))**3 + int(n // k)**3))
