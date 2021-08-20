for _ in range(int(input())):
    (n, m) = tuple(map(int, input().split()))
    a = (n - 1) * m + (m - 1) * n
    b = n * m
    if a <= b:
        print('YES')
    else:
        print('NO')
