n, a = map(int, input().split())
if a % 2:
    print(a // 2 + 1)
else:
    print((n - a) // 2 + 1)
