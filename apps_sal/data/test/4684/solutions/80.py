(r, g, b) = input().split()
ans = int(r + g + b)
if ans % 4 == 0:
    print('YES')
else:
    print('NO')
