(n, k) = map(int, input().split())
if 1 <= k and k <= n:
    print((k - 1) // 2)
elif n + n - 1 < k:
    print(0)
else:
    print((n - (k - n) + 1) // 2)
