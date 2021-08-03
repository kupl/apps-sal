H, W = list(map(int, input().split()))
s = [input() for _ in range(H)]
cells = [(i, j) for i in range(H) for j in range(W)]
di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

for i, j in cells:
    if s[i][j] == '.':
        continue
    flag = False
    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if ni < 0 or nj < 0 or ni >= H or nj >= W:
            continue
        if s[ni][nj] == '#':
            flag = True
    if not flag:
        print("No")
        break
else:
    print("Yes")
