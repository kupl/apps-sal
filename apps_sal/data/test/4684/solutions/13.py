

r, g, b = list(map(str, input().split()))

answer = int(r + g + b)

if answer % 4 == 0:
    print('YES')
else:
    print('NO')
