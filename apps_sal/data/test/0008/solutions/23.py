m = [x for x in input().split()]
tiles = [[0 for i in range(9)] for j in range(3)]
for i in range(len(m)):
    g = int(m[i][0]) - 1
    h = m[i][1]
    if h == 'm':
        tiles[0][g] += 1
    elif h == 'p':
        tiles[1][g] += 1
    else:
        tiles[2][g] += 1
if m[0] == m[1] and m[1] == m[2]:
    print(0)
elif m[0] == m[1]:
    print(1)
elif m[0] == m[2]:
    print(1)
elif m[1] == m[2]:
    print(1)
else:
    n = False
    for i in range(3):
        for j in range(9):
            if tiles[i][j] != 0:
                if j != 8 and tiles[i][j + 1] != 0:
                    if j != 7 and tiles[i][j + 2] != 0:
                        print(0)
                        n = True
                        break
                    else:
                        print(1)
                        n = True
                        break
                elif j != 7 and j != 8 and (tiles[i][j + 2] != 0):
                    print(1)
                    n = True
                    break
    if n == False:
        print(2)
