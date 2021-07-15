import sys


def LI():
    return list(map(int, input().split()))


def LSH(h):
    return [input() for _ in range(h)]


H, W = LI()
masu = LSH(H)
for i in range(H):
    for j in range(W):
        ok = 0
        if masu[i][j] == ".":
            continue
        if j+1 < W:
            if masu[i][j+1] == "#":
                ok = 1
        if j-1 >= 0:
            if masu[i][j-1] == "#":
                ok = 1
        if i+1 < H:
            if masu[i+1][j] == "#":
                ok = 1
        if i-1 >= 0:
            if masu[i-1][j] == "#":
                ok = 1
        if ok == 0:
            print("No")
            return
print("Yes")

