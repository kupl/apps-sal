import math
(n, q) = map(int, input().split())
maxh = int(math.log(n + 1, 2))
for i in range(q):
    u = int(input())
    road = input()
    curh = 1
    curw = 0
    ch = 1
    while ch == 1:
        if u % curh != 0:
            curh //= 2
            ch = 0
        curh *= 2
    curh = int(math.log(curh, 2))
    a = 1 << curh - 1
    b = 1 << curh
    curw = (u - a) // b + 1
    for move in road:
        if move == 'L':
            if curh != 1:
                curh -= 1
                curw = curw * 2 - 1
                u -= 1 << curh - 1
        elif move == 'R':
            if curh != 1:
                curh -= 1
                curw *= 2
                u += 1 << curh - 1
        elif curh != maxh:
            if curw % 2 == 1:
                u = (u + u + (1 << curh)) // 2
                curh += 1
                curw = curw // 2 + 1
            else:
                u = (u + u - (1 << curh)) // 2
                curh += 1
                curw = curw // 2
    print(u)
