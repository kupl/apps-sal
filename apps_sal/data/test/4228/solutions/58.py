n, l = list(map(int, input().split()))
if l >= 0:
    print(((n - 1) * l + (n * (n + 1)) // 2 - (n - 1) - 1))
else:
    if n >= -l + 1:
        print((n * l + (n * (n + 1)) // 2 - n))
    else:
        print(((n - 1) * l + (n * (n + 1)) // 2 - (n - 1) - n))
