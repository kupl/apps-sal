H, W = list(map(int, input().split()))
Grid = [["."] * (W + 2)]
for i in range(H):
    Grid.append(list("." + str(input()) + "."))

Grid.append(["."] * (W + 2))
for k in range(1, H + 1):
    for l in range(1, W + 1):
        moji = Grid[k][l]
        if moji == "
          flg = 0
           for rec, col in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                if Grid[k + rec][l + col] == "
                  Grid[k + rec][l + col] = "b"
                   flg = 1
                elif Grid[k + rec][l + col] == "b":
                    flg = 1

            if flg == 1:
                Grid[k][l] = "b"
            else:
                break
    else:
        continue
    print("No")
    break
else:
    print("Yes")
