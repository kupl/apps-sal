a, b, c = list(map(int, input().split()))
d, e, f = list(map(int, input().split()))
if a > d or a + b > d + e or a + b + c > d + e + f:
    print('NO')
else:
    print('YES')
