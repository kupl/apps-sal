(r, g, b) = map(str, input().split())
number = int(r + g + b)
if number % 4 == 0:
    print('YES')
else:
    print('NO')
