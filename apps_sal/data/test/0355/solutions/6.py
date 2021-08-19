field = [list(input()) for i in range(8)]
for y in range(8):
    for x in range(y + 1, 8):
        (field[x][y], field[y][x]) = (field[y][x], field[x][y])
minW = 1000
minB = 1000
for row in range(8):
    w = None
    for col in range(7, -1, -1):
        if field[row][col] == 'W':
            w = col
    if w != None and 'B' not in field[row][:w]:
        minW = min(minW, w)
    b = None
    for col in range(8):
        if field[row][col] == 'B':
            b = col
    if b != None and 'W' not in field[row][b:]:
        minB = min(minB, 7 - b)
if minB < minW:
    print('B')
else:
    print('A')
