(a, b, c) = map(int, input().split())
x = str(a) + str(b) + str(c)
if int(x) % 4 == 0:
    print('YES')
else:
    print('NO')
