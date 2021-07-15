n = int(input())
xyh = []
for i in range(n):
    xyh.append(list(map(int, input().split())))
xyh.sort(key = lambda x: x[2], reverse = True)
for i in range(101):
    for j in range(101):
        h = xyh[0][2] + abs(xyh[0][0] - i) + abs(xyh[0][1] - j)
        flag = True
        for k in range(1, n):
            if xyh[k][2] == 0:
                if abs(xyh[k][0] - i) + abs(xyh[k][1] - j) < h:
                    flag = False
                    break
            else:
                temp = xyh[k][2] + abs(xyh[k][0] - i) + abs(xyh[k][1] - j)
                if h != temp:
                    flag = False
                    break
        if flag == True and h >= 1:
            print(i, j, h)
            break
    if flag == True:
        break
