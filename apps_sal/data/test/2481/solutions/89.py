H, W = map(int, input().split())
C = [list(map(int, input().split())) for _ in range(10)]
A = [list(map(int, input().split())) for _ in range(H)]

for k in range(10):
    for i in range(10):
        for j in range(10):
            C[i][j] = min(C[i][j], C[i][k] + C[k][j])

answer = 0
for i in range(H):
    for j in range(W):
        if A[i][j] == -1:
            continue
        answer += C[A[i][j]][1]

print(answer)
