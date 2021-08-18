m, s = map(int, input().split())
if m == 1 and s == 0:
    print(0, 0)
    return
if (s == 0 and m > 1) or (s > m * 9):
    print(-1, -1)
else:
    n = (s - 1) // 9
    if n == m - 1:
        print(s - n * 9, '9' * n, sep='', end=' ')
        print('9' * n, s - n * 9, sep='')
    else:
        print('1', '0' * (m - n - 2), s - n * 9 - 1, '9' * n, sep='', end=' ')
        print('9' * n, s - n * 9, '0' * (m - n - 1), sep='')
