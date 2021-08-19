for _ in range(int(input())):
    (n, m) = list(map(int, input().split()))
    sim = False
    for i in range(n):
        (a, b) = list(map(int, input().split()))
        (c, d) = list(map(int, input().split()))
        if c == b:
            sim = True
    if m % 2 == 1:
        print('NO')
    elif sim:
        print('YES')
    else:
        print('NO')
