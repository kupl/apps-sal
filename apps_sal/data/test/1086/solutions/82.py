H, W = map(int, input().split())
A = tuple(tuple(map(int, input().split())) for _ in range(H))
B = tuple(tuple(map(int, input().split())) for _ in range(H))
table = [0] * W
table[0] = 1 << 6400
for i in range(H):
    for j in range(W):
        shamt = abs(A[i][j] - B[i][j])
        if j > 0:
            table[j] |= table[j - 1]
        table[j] = (table[j] << shamt) | (table[j] >> shamt)
dl = dr = 1 << 6400
for i in range(6401):
    if table[W - 1] & (dl | dr):
        print(i)
        break
    dl <<= 1
    dr >>= 1
