N = int(input())
xyh = [list(map(int,input().split())) for i in range(N)]
f = False
for x in range(101):
    for y in range(101):
        for i in range(N):
            if xyh[i][2] != 0:
                H = abs(xyh[i][0]-x) + abs(xyh[i][1]-y) + xyh[i][2]
                break
        for i in range(N):
            if xyh[i][2] == 0 and H - abs(xyh[i][0]-x) - abs(xyh[i][1]-y) > 0:
                break
            if xyh[i][2] != 0 and H != abs(xyh[i][0]-x) + abs(xyh[i][1]-y) + xyh[i][2]:
                break
        else:
            f = True
            break
    if f:
        break
print(x,y,H)
