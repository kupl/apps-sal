def __starting_point():
    k = int(input())
    (a, b) = list(map(int, input().split()))
    flg = False
    for i in range(a, b + 1):
        if i % k == 0:
            flg = True
            break
    if flg:
        print('OK')
    else:
        print('NG')


__starting_point()
