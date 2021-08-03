# 今の座標の色が#のとき、上下左右いずれかに#があればおｋ
h, w = list(map(int, input().split()))
table = [input() for _ in range(h)]
step = [0, 1, 0, -1, 0]
for i in range(h):
    for j in range(w):
        if table[i][j] == ".":
            continue
        flag = False
        for k in range(4):
            ny, nx = i + step[k], j + step[k + 1]
            if nx < 0 or nx == w or ny < 0 or ny == h:
                continue
            if table[ny][nx] == "#":
                flag = True
        if flag == False:
            print("No")
            return
print("Yes")
