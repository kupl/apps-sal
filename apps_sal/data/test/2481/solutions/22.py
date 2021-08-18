H, W = list(map(int, input().split()))

C = []
for i in range(10):
    tmp = list(map(int, input().split()))
    C.append(tmp)

A = []
for i in range(H):
    tmp = list(map(int, input().split()))
    A.append(tmp)

for i in range(10):
    for j in range(10):
        for k in range(10):
            C[j][k] = min(C[j][k], C[j][i] + C[i][k])

ans = 0
for h in range(H):
    for w in range(W):
        if A[h][w] == -1 or A[h][w] == 1:
            continue

        ans += C[A[h][w]][1]
print(ans)
