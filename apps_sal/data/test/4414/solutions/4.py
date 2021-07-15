for _ in range(int(input())):
    a, b, n, S = list(map(int, input().split()))
    if b >= S % n and a * n + b >= S:
        print('YES')
    else:
        print('NO')

