(n, m) = map(int, input().split())
if m < n - 1:
    print('-1')
elif m == n - 1:
    print('0' + '10' * m)
elif m == n:
    print('10' * m)
elif m == n + 1:
    print('10' * n + '1')
else:
    k = m - (n + 1)
    if k > n + 1:
        print('-1')
    elif k == n + 1:
        print('110' * n + '11')
    else:
        print('110' * k + '10' * (n - k) + '1')
