n = int(input())
kx, ky = map(int, input().split())
nearest = [None] * 8
for i in range(n):
    ft, fx, fy = input().split()
    fx = int(fx)
    fy = int(fy)
    if kx == fx:
        if ky > fy:
            if not nearest[0] or nearest[0][1] < fy:
                nearest[0] = (ft, fy)
        else:
            if not nearest[1] or nearest[1][1] > fy:
                nearest[1] = (ft, fy)
    elif ky == fy:
        if kx > fx:
            if not nearest[2] or nearest[2][1] < fx:
                nearest[2] = (ft, fx)
        else:
            if not nearest[3] or nearest[3][1] > fx:
                nearest[3] = (ft, fx)
    elif kx + ky == fx + fy:
        if kx - ky > fx - fy:
            if not nearest[4] or nearest[4][1] < fx - fy:
                nearest[4] = (ft, fx - fy)
        else:
            if not nearest[5] or nearest[5][1] > fx - fy:
                nearest[5] = (ft, fx - fy)
    elif kx - ky == fx - fy:
        if kx + ky > fx + fy:
            if not nearest[6] or nearest[6][1] < fx + fy:
                nearest[6] = (ft, fx + fy)
        else:
            if not nearest[7] or nearest[7][1] > fx + fy:
                nearest[7] = (ft, fx + fy)

res = "NO"
for i in range(4):
    if nearest[i] and nearest[i][0] != "B":
        res = "YES"
for i in range(4, 8):
    if nearest[i] and nearest[i][0] != "R":
        res = "YES"
print(res)
