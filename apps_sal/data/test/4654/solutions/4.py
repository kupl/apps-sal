for _ in range(int(input())):
    (n, k) = map(int, input().split())
    odd = n - k + 1
    even = n - (k - 1) * 2
    if odd > 0 and odd % 2 == 1:
        print('YES')
        print('1 ' * (k - 1), odd, sep='')
    elif even > 0 and even % 2 == 0:
        print('YES')
        print('2 ' * (k - 1), even, sep='')
    else:
        print('NO')
