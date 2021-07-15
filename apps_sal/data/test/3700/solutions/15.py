n, k = list(map(int, input().split()))
if n >= k:
    print((k - 1) // 2)
else:
    if n - k // 2 >= 0:
        print(n - k // 2)
    else:
        print(0)

