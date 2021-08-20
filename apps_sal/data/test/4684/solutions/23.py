(r, g, b) = map(str, input().split())
RGB = r + g + b
if int(RGB) % 4 == 0:
    print('YES')
else:
    print('NO')
