H, W = map(int, input().split())
x = [list(map(str, list(input()))) for l in range(H)]

#両端にドットを追加
for i in range(len(x)):
    x[i].insert(0, ".")
    x[i].append(".")
#最上部と最下部の行にドットを追加
x.insert(0, ["."]*(W+2))
x.append(["."]*(W+2))

#3*3→5*5 from[1][1] to[3][3] to[H][W]
tmp = 0
for i in range(1, H+1):
    for j in range(1, W+1):
        if x[i][j] == "#":
            x[i][j] = "#"
            continue
        if x[i-1][j-1] == "#":
            tmp += 1
        if x[i-1][j] == "#":
            tmp += 1
        if x[i-1][j+1] == "#":
            tmp += 1
        if x[i][j-1] == "#":
            tmp += 1
        if x[i][j+1] == "#":
            tmp += 1
        if x[i+1][j-1] == "#":
            tmp += 1
        if x[i+1][j] == "#":
            tmp += 1
        if x[i+1][j+1] == "#":
            tmp += 1
        x[i][j] = str(tmp)
        tmp = 0
#最上部と最下部の行のドットを削除
del x[0]
del x[-1]
#両端のドットを削除
for i in range(len(x)):
    del x[i][0]
    del x[i][-1]

for i in range(len(x)):
    print(''.join(x[i]))
