(r, g, b) = map(int, input().split())
num = int(str(r) + str(g) + str(b))
if (1 <= r and r <= 9) and (1 <= g and g <= 9) and (1 <= b and b <= 9):
    if num % 4 == 0:
        print('YES')
    else:
        print('NO')
