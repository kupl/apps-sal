(h, w) = map(int, input().split())
inpL = []
isTrue = False
for z in range(h):
    inpL.append(list(str(input())))
for i in range(1, h - 1):
    for j in range(1, w - 1):
        if inpL[i][j] == '*':
            if inpL[i + 1][j] == '*':
                if inpL[i - 1][j] == '*':
                    if inpL[i][j + 1] == '*':
                        if inpL[i][j - 1] == '*':
                            isTrue = True
                            x = i + 0
                            while x >= 0:
                                if inpL[x][j] == '*':
                                    inpL[x][j] = '.'
                                else:
                                    break
                                x -= 1
                            x = i + 1
                            while x < h:
                                if inpL[x][j] == '*':
                                    inpL[x][j] = '.'
                                else:
                                    break
                                x += 1
                            y = j - 1
                            while y >= 0:
                                if inpL[i][y] == '*':
                                    inpL[i][y] = '.'
                                else:
                                    break
                                y -= 1
                            y = j + 1
                            while y < w:
                                if inpL[i][y] == '*':
                                    inpL[i][y] = '.'
                                else:
                                    break
                                y += 1
                            break
    if isTrue:
        break
if isTrue:
    isTrue = True
    for i in range(h):
        if '*' in inpL[i]:
            isTrue = False
            break
    if isTrue:
        print('YES')
    else:
        print('NO')
else:
    print('NO')
