N = int(input())
xyh = [list(map(int, input().strip().split())) for _ in range(N)]

dp = [[-1 for i in range(101)] for j in range(101)]
for n in range(N):
    dp[xyh[n][0]][xyh[n][1]] = xyh[n][2]


def find_top(x, y, N, xyh):
    find = True
    prev = -1
    for n in range(N):
        if xyh[n][2] != 0:
            top = xyh[n][2] + abs(xyh[n][0] - x) + abs(xyh[n][1] - y)
            if prev == -1:
                prev = top
            else:
                if prev != top:
                    find = False
                    break
    return find, top


def check_top(x, y, top, N, xyh):
    check = True
    for n in range(N):
        if xyh[n][2] == 0:
            if top - abs(xyh[n][0] - x) - abs(xyh[n][1] - y) > 0:
                check = False
                break
    return check


fin = False
for x in range(101):
    if fin == True:
        break
    for y in range(101):
        find = find_top(x, y, N, xyh)[0]
        height = find_top(x, y, N, xyh)[1]
        if find and height >= 1 and check_top(x, y, height, N, xyh):
            print("{} {} {}".format(x, y, height))
            fin = True
