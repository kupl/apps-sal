(n, l) = map(int, input().split())
if l + n - 1 < 0:
    print((n - 1) * (l - 1) + n * (n - 1) // 2)
elif l > 0:
    print(n * (l - 1) + n * (n + 1) // 2 - l)
else:
    print(n * (l - 1) + n * (n + 1) // 2)
