arr = [[3, 3, 4, 4, 3, 3],
[3, 3, 4, 4, 3, 3],
[2, 2, 3, 3, 2, 2],
[2, 2, 3, 3, 2, 2],
[1, 1, 2, 2, 1, 1],
[1, 1, 2, 2, 1, 1]]

bestX = -1
bestY = -1
bestI = -1

lines = [''] * 6
for i in range(6):
    lines[i] = input()
    cnt = 0
    for j in range(8):
        if lines[i][j] == '.':
            if bestX == -1 or arr[bestY][bestX] < arr[i][cnt]:
                bestY, bestX, bestI = i, cnt, j

        if j != 2 and j != 5:
            cnt += 1

lines[bestY] = lines[bestY][:bestI] + 'P' + lines[bestY][bestI + 1:]


for i in range(6):
    print(lines[i])

