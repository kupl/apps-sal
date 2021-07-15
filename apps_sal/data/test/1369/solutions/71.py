from math import sqrt

N = int(input())
XY = [tuple(map(int, input().split())) for _ in range(N)]

def calc(r): #半径rが与えられたときに全てが重なるかを判定
    lst = [] #交点を入れるリスト
    for i in range(N - 1):
        x1 = XY[i][0]
        y1 = XY[i][1]
        for j in range(i + 1, N):
            x2 = XY[j][0]
            y2 = XY[j][1]
            diff = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

            if diff > 2 * r:
                return False
            
            h = sqrt(r ** 2 - (diff / 2) ** 2)
            
            if x1 == x2:
                ny = (y1 + y2) / 2
                lst.append([x1 - h, ny])
                lst.append([x1 + h, ny]) 
            elif y1 == y2:
                nx = (x1 + x2) / 2
                lst.append([nx, y1 - h])
                lst.append([nx, y1 + h])
            else:
                a = (y2 - y1) / (x2 - x1) #2点を結ぶ直線の傾き

                b = -1 / a

                size = sqrt(1 + b ** 2)

                nx = h / size
                ny = nx * b

                #もとの2点の中点
                xc = (x1 + x2) / 2
                yc = (y1 + y2) / 2

                lst.append([xc + nx, yc + ny])
                lst.append([xc - nx, yc - ny])
    # print (r)
    # print (lst)
    nr = r + eps
    for x, y in lst: #中心の点
        flag = True
        for X, Y in XY:
            tmp = (x - X) ** 2 + (y - Y) ** 2
            if tmp > nr ** 2:
                flag = False
                break
        if flag:
            return True
          
    
l = 0
r = 1000

eps = 10 ** (-9)

for i in range(100):
    mid = (l + r) / 2
    if calc(mid):
        r = mid
    else:
        l = mid

print (r)

