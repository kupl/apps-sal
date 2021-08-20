faces = [[5, 6, 17, 18, 21, 22, 13, 14], [7, 8, 19, 20, 23, 24, 15, 16], [1, 3, 5, 7, 9, 11, 24, 22], [2, 4, 6, 8, 10, 12, 23, 21], [3, 4, 17, 19, 10, 9, 16, 14], [1, 2, 18, 20, 12, 11, 15, 13]]
cube = input().split(' ')


def legit(cube):
    for i in range(6):
        for j in range(4):
            if cube[4 * i] != cube[4 * i + j]:
                return False
    return True


t = False
for rotato in faces:
    cubea = cube.copy()
    for i in range(8):
        cubea[rotato[i] - 1] = cube[rotato[(i + 2) % 8] - 1]
    cubeb = cubea.copy()
    for i in range(8):
        cubeb[rotato[i] - 1] = cubea[rotato[(i + 2) % 8] - 1]
    cubec = cubeb.copy()
    for i in range(8):
        cubec[rotato[i] - 1] = cubeb[rotato[(i + 2) % 8] - 1]
    if legit(cubea) or legit(cubec):
        t = True
if not t:
    print('NO')
else:
    print('YES')
