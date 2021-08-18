for _ in range(int(input())):
    n = int(input())
    x = 6 + 10 + 14
    if x + 1 > n:
        print('NO')
        continue
    y = n - x
    if y not in (6, 10, 14):
        print('YES')
        print(6, 10, 14, y)
        continue
    x += 1
    y -= 1
    if y == 0:
        print('NO')
    else:
        print('YES')
        print(6, 10, 15, y)
