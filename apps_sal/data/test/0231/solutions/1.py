n, a = map(int, input().split())

if a % 2:
    print(a // 2 + 1)
else:
    print(n // 2 - a // 2 + 1)
