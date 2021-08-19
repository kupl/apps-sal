for _ in range(int(input())):
    (n, m) = list(map(int, input().split()))
    if n == m and n == 2:
        print('YES')
    elif n >= 2 and m >= 2:
        print('NO')
    else:
        print('YES')
