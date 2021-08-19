(r, g, b) = input().split()
a = r + g + b
if int(a) % 4 == 0:
    print('YES')
else:
    print('NO')
