def __starting_point():
    N = int(input())
    su = 0
    sl = 0
    canF = False
    for i in range(N):
        arr = input().split(' ')
        a = int(arr[0])
        b = int(arr[1])
        if (a % 2 == 0 and b % 2 == 1) or (a % 2 == 1 and b % 2 == 0):
            canF = True
        su += a
        sl += b
    ans = -1
    if (su + sl) % 2 == 1:
        ans = -1
    else:
        if su % 2 == 0 and sl % 2 == 0:
            ans = 0
        elif canF:
            ans = 1
        else:
            ans = -1
    print(ans)


__starting_point()
