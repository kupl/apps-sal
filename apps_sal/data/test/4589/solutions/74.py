import sys

H, W = map(int, input().split())
l = []
for i in range(H):
    l.append(list(input()))

for i in range(H):
    for j in range(W):
        c = 0

        if l[i][j] == "
        pass

        else:
            if 0 < i and 0 < j and l[i - 1][j - 1] == '
            c += 1
            if 0 < i and l[i - 1][j] == '
            c += 1
            if 0 < i and j < W - 1 and l[i - 1][j + 1] == '
            c += 1
            if 0 < j and l[i][j - 1] == '
            c += 1
            if j < W - 1 and l[i][j + 1] == '
            c += 1
            if i < H - 1 and 0 < j and l[i + 1][j - 1] == '
            c += 1
            if i < H - 1 and l[i + 1][j] == '
            c += 1
            if i < H - 1 and j < W - 1 and l[i + 1][j + 1] == '
            c += 1

            l[i][j] = str(c)

for i in range(H):
    print(''.join(l[i]))
