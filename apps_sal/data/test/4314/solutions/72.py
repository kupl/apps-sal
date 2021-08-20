(H, W) = map(int, input().split())
a = [input() for i in range(H)]
b = [0] * W
c = [0] * H
for i in range(H):
    cnt = 0
    for j in range(W):
        if a[i][j] == '#':
            b[j] += 1
            cnt += 1
    c[i] = cnt
for i in range(H):
    if c[i] == 0:
        continue
    for j in range(W):
        if b[j] != 0:
            print(a[i][j], end='')
    print()
