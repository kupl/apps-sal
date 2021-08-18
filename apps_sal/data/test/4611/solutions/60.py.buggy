N = int(input())

locx = 0
locy = 0
time = 0
for i in range(N):
    t, x, y = map(int, input().split())
    nowtime = t - time
    dis = abs(locx - x) + abs(locy - y)
    if (nowtime - dis) < 0:
        print("No")
        return
    if (nowtime - dis) % 2 == 1:
        print("No")
        return

    time = t
    locx = x
    locy = y


else:
    print("Yes")
