H, W = list(map(int, input().split()))
sq = [list(input()) for i in range(H)]
ans = False
c = H * W
pos = [[0, 0, 0]]

while pos != []:
    y, x, depth = pos.pop(0)

    if x == W - 1 and y == H - 1:
        ans = True
        break

    if 0 <= x + 1 <= W - 1:
        if sq[y][x + 1] == ".":
            pos.append([y, x + 1, depth + 1])
            sq[y][x + 1] = "!"

    if 0 <= x - 1 <= W - 1:
        if sq[y][x - 1] == ".":
            pos.append([y, x - 1, depth + 1])
            sq[y][x - 1] = "!"

    if 0 <= y + 1 <= H - 1:
        if sq[y + 1][x] == ".":
            pos.append([y + 1, x, depth + 1])
            sq[y + 1][x] = "!"

    if 0 <= y - 1 <= H - 1:
        if sq[y - 1][x] == ".":
            pos.append([y - 1, x, depth + 1])
            sq[y - 1][x] = "!"


for j in range(H):
    for k in range(W):
        if sq[j][k] == "
        c -= 1

if ans == True:
    print((c - depth - 1))
else:
    print((-1))
