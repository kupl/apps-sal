for _ in range(int(input())):
    (a, b, c, n) = map(int, input().split())
    mm = max(a, b, c)
    n -= mm - a
    n -= mm - b
    n -= mm - c
    if n >= 0 and n % 3 == 0:
        print('YES')
    else:
        print('NO')
