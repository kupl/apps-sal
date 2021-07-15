a, b, c, d = map(int, input().split())
if b < c or d < a:
    print(0)
elif a <= c and d <= b:
    print(d-c)
elif c <= a and b <= d:
    print(b-a)
elif a <= c and b <= d:
    print(b-c)
elif c <= a and d <= b:
    print(d-a)
