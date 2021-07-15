H, W = list(map(int, input().split()))
C = []
for _ in range(10):
    c = list(map(int, input().split()))
    C.append(c)

A = []
for _ in range(H):
    a = list(map(int, input().split()))
    A.append(a)

# 0-9を1に変える時の最小のエネルギーをそれぞれ求める(ワーシャルフロイド法)
for k in range(10):
    for i in range(10):
        for j in range(10):
            C[i][j] = min(C[i][j], C[i][k] + C[k][j])

count = 0
for i in range(H):
    for j in range(W):
        if (A[i][j] == -1):
            continue
        else:
            count += C[A[i][j]][1]

print(count)

