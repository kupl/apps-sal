for __ in range(int(input())):
    n, m, k = map(int, input().split())
    arr = list(map(int, input().split()))
    flg = True
    for f, nx in zip(arr, arr[1:]):
        tg = max(nx - k, 0)
        m -= tg - f
        if m < 0:
            flg = False
    print('YES' if flg else 'NO')
