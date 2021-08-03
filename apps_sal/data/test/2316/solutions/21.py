for i in range(int(input())):
    x, n, m = list(map(int, input().split()))
    if x - m * 10 <= 0:
        print('YES')
    else:
        for j in range(n):
            x = x // 2 + 10
        x -= 10 * m
        if x <= 0:
            print('YES')
        else:
            print('NO')
