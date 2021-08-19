for _ in range(int(input())):
    (x, y, z) = map(int, input().split())
    (a, b, c) = (min(x, y), min(x, z), min(y, z))
    if x == max(a, b) and y == max(a, c) and (z == max(b, c)):
        print('YES')
        print(a, b, c)
    else:
        print('NO')
