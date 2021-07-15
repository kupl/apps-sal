n, k = list(map(int, input().split()))
if k <= n:
    print((k - 1) // 2)
else:
    print(max(0, (k - 1) // 2 - (k - n) + 1))


