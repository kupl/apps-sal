n, a = list(map(int, input().split()))

if a % 2 == 0:
    print((n - a) // 2 + 1)
else:
    print(a // 2 + 1)
