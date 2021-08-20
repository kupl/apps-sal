for _ in range(int(input())):
    (a, b, c, n) = [int(s) for s in input().split()]
    (a, b, c) = sorted([a, b, c])
    w = c - a + c - b
    if w > n:
        print('NO')
    elif (n - w) % 3 == 0:
        print('YES')
    else:
        print('NO')
