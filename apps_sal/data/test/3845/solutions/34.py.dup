A, B = map(int, input().split())

a = 626 - A
b = 530 - B

H, W = 99, 99
S = [["."] * W for _ in range(H)]
for i in range(H):
    for j in range(W):

        if i == 0 or i == H - 1:
            S[i][j] = "#"
            continue
        if j == 0 or j == W - 1:
            S[i][j] = "#"
            continue

        if i % 4 == 0 or i % 4 == 2:
            if j % 4 == 3:
                S[i][j] = "."
            else:
                S[i][j] = "#"
        elif i % 4 == 1:
            if j % 4 == 0 or j % 4 == 2:
                S[i][j] = "#"

h, w = 1, 1
while a != 0:
    S[h][w] = "#"
    a -= 1
    w += 4
    if w >= W:
        w = 1
        h += 4

h, w = 4, 3
while b != 0:
    S[h][w] = "#"
    b -= 1
    w += 4
    if b == 0:
        break
    if w >= W - 4:
        h += 3
        S[h][0] = "#"
        w = 3
        h += 1

print(99, 99)
for i in range(H):
    output = "".join(S[i])
    print(output)
