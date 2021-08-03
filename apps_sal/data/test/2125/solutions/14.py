
def countFlagNum(x):
    y = 0
    flagNum = 0
    while y < m:
        curColor = a[x][y]
        colorCountByX = 1
        isItFlag = True
        while x + colorCountByX < n and a[x + colorCountByX][y] == curColor:
            colorCountByX += 1
        if not(x + colorCountByX * 3 > n):
            color2 = a[x + colorCountByX][y]
            color3 = a[x + colorCountByX * 2][y]
            if color3 != color2 and color2 != curColor:
                offY = 0
                while y + offY < m and isItFlag:
                    i = 0
                    while i < colorCountByX and isItFlag:
                        if (a[x + i][y + offY] != curColor or a[x + colorCountByX + i][y + offY] != color2 or a[x + colorCountByX * 2 + i][y + offY] != color3):
                            isItFlag = False
                            if offY == 0:
                                offY = 1
                        i += 1
                    if isItFlag:
                        flagNum = flagNum + 1 + offY
                        offY += 1
                y += offY - 1
        y += 1
    return flagNum


n, m = list(map(int, input().split()))
a = []
totalFlagNum = 0

for i in range(n):
    row = input()
    a.append(row)

for i in range(n - 2):
    totalFlagNum += countFlagNum(i)

print(totalFlagNum)
