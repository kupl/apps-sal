r, g, b = list(map(int, input().split()))

if 1 <= r and g and b <= 9:
    if ((r * 100) + (g * 10) + b) % 4 == 0:
        print('YES')
    else:
        print('NO')
