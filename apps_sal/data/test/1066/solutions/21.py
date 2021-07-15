n, k = map(int, input().split())
if k <= (n + 1) // 2:
    print(k + k - 1)
else:
    k -= (n + 1) // 2
    print(k + k)
