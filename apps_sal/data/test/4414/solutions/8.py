for _ in range(int(input())):
    (a, b, n, s) = map(int, input().split())
    s -= min(a, s // n) * n
    if b >= s:
        print('YES')
    else:
        print('NO')
