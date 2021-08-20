(n, k) = list(map(int, input().split()))
if n >= k:
    print((k - 1) // 2)
elif n - k // 2 >= 0:
    print(n - k // 2)
else:
    print(0)
