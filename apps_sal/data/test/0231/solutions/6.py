
n, a = map(int, input().split())
if a % 2 == 1:
    print(int(a // 2 + 1))
    return
else:
    print(int(n / 2 + 1 - a // 2))
    return
