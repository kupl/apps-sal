a, b, c, d, e, f = list(map(int, input().split()))
if (a + b + c == d + e + f):
    print('YES')
elif (a + b + d == c + e + f):
    print('YES')
elif (a + b + e == c + d + f):
    print('YES')
elif (a + b + f == c + d + e):
    print('YES')
elif (a + c + d == b + e + f):
    print('YES')
elif (a + c + e == b + d + f):
    print('YES')
elif (a + c + f == b + d + e):
    print('YES')
elif (a + d + e == b + c + f):
    print('YES')
elif (a + d + f == b + c + e):
    print('YES')
elif (a + e + f == b + c + d):
    print('YES')
else:
    print('NO')
