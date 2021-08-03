n, k = map(int, input().split())
if k >= n - 1:
    print(n - 1)
else:
    print(k + ((n - k) * (n - k + 1)) // 2 - 1)
