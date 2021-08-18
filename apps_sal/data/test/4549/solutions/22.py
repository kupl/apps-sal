from itertools import product
H, W = map(int, input().split())
S = [input() for i in range(H)]

isOK = True

for y, x in product(range(H), range(W)):
    if S[y][x] == '.':
        continue
    sum = 0

    if 0 < x:
        if S[y][x - 1] == '
        sum += 1

    if x < W - 1:
        if S[y][x + 1] == '
        sum += 1

    if 0 < y:
        if S[y - 1][x] == '
        sum += 1

    if y < H - 1:
        if S[y + 1][x] == '
        sum += 1

    if sum == 0:
        isOK = False

if isOK:
    print("Yes")
else:
    print("No")
