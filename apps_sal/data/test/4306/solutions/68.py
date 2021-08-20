(a, b, c, d) = map(int, input().split())
if b < c or a > d:
    print('0')
elif a <= c and b >= d:
    print(d - c)
elif a >= c and b <= d:
    print(b - a)
elif b < d:
    print(b - c)
elif b > d:
    print(d - a)
