(r, g, b) = map(int, input().split())
if 1 <= r <= 9 and 1 <= g <= 9 and (1 <= b <= 9) and ((100 * r + 10 * g + b) % 4 == 0):
    print('YES')
else:
    print('NO')
