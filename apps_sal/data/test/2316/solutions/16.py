for _ in range(int(input())):
    x, n, m = list(map(int, input().split()))
    for _ in range(n):
        if x // 2 + 10 < x:
            x = x // 2 + 10
        else:
            break
    x -= m * 10
    print('YES' if x <= 0 else 'NO')
