n, m, k = [int(s) for s in input().split()]
n, m = max(n, m), min(n, m)
if n + m - 2 < k: print(-1)
elif n - 1 < k:
    print(m // (k - n + 2))
elif m - 1 < k: print(n // (k + 1) * m)
else:
    print(max(n // (k + 1) * m, m // (k + 1) * n))
