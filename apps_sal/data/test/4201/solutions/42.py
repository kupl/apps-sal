H, W, K = map(int, input().split())
List = [list(input()) for _ in range(H)]

MAP = [[0 for j in range(W)] for i in range(H)]

for i in range(H):
    for j in range(W):
        if List[i][j] == '
        MAP[i][j] = 1

MAPP = [[0 for j in range(W)] for i in range(H)]
bx = [0] * W
by = [0] * H
c = [0] * 2**H * 2**W
for i in range(2**H * 2**W):
    b = format(i, 'b').zfill(H + W)
    for jx in range(W):
        bx[jx] = int(b[-W + jx])
    for jy in range(H):
        by[jy] = int(b[jy])
    for k in range(H):
        for l in range(W):
            MAPP[k][l] = MAP[k][l] * bx[l] * by[k]
    c[i] = sum(map(sum, MAPP))

print(c.count(K))
