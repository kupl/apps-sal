(a, b, c) = input().split()
a = int(a)
b = int(b)
c = int(c)
if a + b >= c:
    if a <= c:
        print('YES')
    else:
        print('NO')
else:
    print('NO')
