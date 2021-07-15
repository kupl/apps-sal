a, b = map(int, input().split())
if a == b:
    print(a * 10, b * 10 + 1)
elif b - 1 == a:
    print(a, b)
elif b == 1 and a == 9:
    print(a, b * 10)
else:
    print(-1)
