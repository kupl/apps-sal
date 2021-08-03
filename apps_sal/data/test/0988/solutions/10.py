room = []

values = [[3, 3, 0, 4, 4, 0, 3, 3], [3, 3, 0, 4, 4, 0, 3, 3], [2, 2, 0, 3, 3, 0, 2, 2], [2, 2, 0, 3, 3, 0, 2, 2], [1, 1, 0, 2, 2, 0, 1, 1], [1, 1, 0, 2, 2, 0, 1, 1]]

for i in range(6):
    room.append(input())

px, py = -1, -1
best = -1
for i in range(6):
    for j in range(8):
        if room[i][j] == '.' and best < values[i][j]:
            px, py = i, j
            best = values[i][j]
ans = []
for i in range(6):
    if px != i:
        ans.append(room[i])
    else:
        ans.append((room[i])[:py] + 'P' + (room[i])[py + 1:])
for i in range(6):
    print(ans[i])
