a, b = map(int, input().split())
if a // 10 != 0 or b // 10 != 0:
    print(-1)
else:
    print(a*b)
