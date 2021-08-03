a, p = map(int, input().split())

if a <= 5:
    print(0)
elif 6 <= a <= 12:
    print(p // 2)
elif a >= 13:
    print(p)
