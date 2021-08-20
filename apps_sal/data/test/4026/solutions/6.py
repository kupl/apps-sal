for _ in range(int(input())):
    (n, m) = tuple(map(int, input().split()))
    res = False
    for i in range(n):
        (a, b) = tuple(map(int, input().split()))
        (c, d) = tuple(map(int, input().split()))
        if b == c:
            res = True
    if m % 2 == 0 and res:
        print('YES')
    else:
        print('NO')
