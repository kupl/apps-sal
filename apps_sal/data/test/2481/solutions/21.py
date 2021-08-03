H, W = [int(_) for _ in input().split()]
C = [[int(_) for _ in input().split()] for _ in range(10)]
A = [[int(_) for _ in input().split()] for _ in range(H)]

for k in range(10):
    for i in range(10):
        for j in range(10):
            C[i][1] = min(C[i][1], C[i][j] + C[j][1])

ans = 0
for h in range(H):
    for w in range(W):
        if A[h][w] != -1:
            v = A[h][w]
            ans += C[v][1]
print(ans)
