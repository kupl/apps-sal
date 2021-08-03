n, d = list(map(int, input().split(' ')))
for i in range(int(input())):
    x, y = list(map(int, input().split(' ')))
    if (y <= (x + d)) and (y >= (x - d)) and (y >= (-x + d)) and (y <= (-x + 2 * n - d)):
        print('YES')
    else:
        print('NO')
