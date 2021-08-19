(H, W) = map(int, input().split())
N = int(input())
A = list(map(int, input().split()))
B = [[0] * W for _ in range(H)]
X = []
for (i, a) in enumerate(A):
    X += [i + 1] * a
for i in range(H):
    for j in range(W):
        if i % 2 == 0:
            B[i][j] = X[i * W + j]
        else:
            B[i][W - j - 1] = X[i * W + j]
for i in range(H):
    print(*B[i])
