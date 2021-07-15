r, g, b = list(map(str, input().split()))
if int(r + g + b) % 4 == 0:
    print('YES')
else:
    print('NO')
