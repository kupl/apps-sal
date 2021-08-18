
r, g, b = map(int, input().split())
answer = 100 * r + 10 * g + b

if answer % 4 == 0:
    print('YES')
else:
    print('NO')
