r, g, b = list(map(int, input().split()))
rgb = int(r * 100 + g * 10 + b)
if rgb % 4 == 0:
    print('YES')
else:
    print('NO')
