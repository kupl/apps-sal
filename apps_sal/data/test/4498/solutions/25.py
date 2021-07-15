a, b, c, d = map(int, input().split())

AB = abs(b - a)
BC = abs(c - b)
AC = abs(c - a)

if (AB <= d and BC <= d) or AC <= d:
    print('Yes')
else:
    print('No')
