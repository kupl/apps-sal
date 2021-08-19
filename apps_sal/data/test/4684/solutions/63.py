(r, g, b) = input().split()
a = int(r + g + b)
if a % 4 == 0:
    print('YES')
else:
    print('NO')
