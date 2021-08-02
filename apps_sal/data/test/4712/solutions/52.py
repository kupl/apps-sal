H, W = map(int, input().split())


frame = [['#' for _ in range(W + 2)] for _ in range(H + 2)]

mat = [['#' for _ in range(W)] for _ in range(H)]
for i in range(H):
    line = input()
    for j in range(W):
        mat[i][j] = line[j]

for i, row in enumerate(mat):
    for j, char in enumerate(row):
        frame[i + 1][j + 1] = char

for i in frame:
    for j in i:
        print(j, end="")
    print()
