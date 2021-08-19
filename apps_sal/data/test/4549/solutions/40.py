H, W = map(int, input().split())
List = [list(input()) for i in range(H)]
res = "Yes"
flag = True


def checkAround(ListX, i, j):
    if i == 0 and j == 0:
        if List[i + 1][j] == "#" or List[i][j + 1] == "#":
            return True
        else:
            return False
    elif i == 0 and j != 0 and j != W - 1:
        if List[i + 1][j] == "#" or List[i][j - 1] == "#" or List[i][j + 1] == "#":
            return True
        else:
            return False
    elif i == 0 and j == W - 1:
        if List[i + 1][j] == "#" or List[i][j - 1] == "#":
            return True
        else:
            return False
    elif i != 0 and i != H - 1 and j == 0:
        if List[i + 1][j] == "#" or List[i - 1][j] == "#" or List[i][j + 1] == "#":
            return True
        else:
            return False
    elif i == H - 1 and j == W - 1:
        if List[i - 1][j] == "#" or List[i][j - 1] == "#":
            return True
        else:
            return False
    elif i == H - 1 and j != 0 and j != W - 1:
        if List[i - 1][j] == "#" or List[i][j + 1] == "#" or List[i][j - 1] == "#":
            return True
        else:
            return False
    elif i == H - 1 and j == 0:
        if List[i - 1][j] == "#" or List[i][j - 1] == "#":
            return True
        else:
            return False
    elif i != 0 and i != H - 1 and j == W - 1:
        if List[i + 1][j] == "#" or List[i - 1][j] == "#" or List[i][j - 1] == "#":
            return True
        else:
            return False
    else:
        if List[i + 1][j] == "#" or List[i - 1][j] == "#" or List[i][j - 1] == "#" or List[i][j + 1] == "#":
            return True
        else:
            return False


for k in range(H):
    for l in range(W):
        if List[k][l] == ".":
            pass
        else:
            flag = checkAround(List, k, l)
            if not flag:
                res = "No"
                break
    if not flag:
        break
print(res)
