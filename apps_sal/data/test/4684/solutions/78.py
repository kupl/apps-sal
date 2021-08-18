r, g, b = map(int, input().split())

answer = (r * 100 + g * 10 + b) % 4
if answer == 0:
    print('YES')
else:
    print('NO')
