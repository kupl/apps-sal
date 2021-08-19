(n, a) = map(int, input().split())
if a % 2 == 1:
    print(1 + a // 2)
else:
    print(1 + (n - a) // 2)
