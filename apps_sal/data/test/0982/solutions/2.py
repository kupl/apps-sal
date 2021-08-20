for __ in range(int(input())):
    (a, b) = list(map(int, input().split()))
    x = b + 1
    if a % x >= x / 2:
        print('YES')
    else:
        print('NO')
