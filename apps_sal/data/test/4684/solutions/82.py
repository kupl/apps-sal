(r, g, b) = list(map(str, input().split()))
v = int(r + g + b)
if v % 4 == 0:
    print('YES')
else:
    print('NO')
