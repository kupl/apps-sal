import sys

H, W = map(int, input().split())
l = []
for i in range(H):
    l.append(list(input()))

for i in range(H):
    for j in range(W):
        c = 0

        if l[i][j] == "#":
            pass

        else:
            # 左上
            if 0 < i and 0 < j and l[i - 1][j - 1] == '#':
                c += 1
            # 上
            if 0 < i and l[i - 1][j] == '#':
                c += 1
            # 右上
            if 0 < i and j < W - 1 and l[i - 1][j + 1] == '#':
                c += 1
            # 左
            if 0 < j and l[i][j - 1] == '#':
                c += 1
            # 右
            if j < W - 1 and l[i][j + 1] == '#':
                c += 1
            # 左下
            if i < H - 1 and 0 < j and l[i + 1][j - 1] == '#':
                c += 1
            # 下
            if i < H - 1 and l[i + 1][j] == '#':
                c += 1
            # 右下
            if i < H - 1 and j < W - 1 and l[i + 1][j + 1] == '#':
                c += 1

                # 地雷隣接数を記載
            l[i][j] = str(c)

# 出力
for i in range(H):
    print(''.join(l[i]))
