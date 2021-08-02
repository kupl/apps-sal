a, b, c, d = map(int, input().split())
if b <= c or d <= a:
    print(0)
elif a <= c:
    print(min(b, d) - c)
elif a >= c:
    print(min(b, d) - a)
