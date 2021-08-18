H, W = [int(x) for x in input().split()]
A = [input().strip() for _ in range(H)]

B = []
for i in range(H):
    if "
    B.append(A[i])

ans = []
for j in range(W):
    for i in range(len(B)):
        if "
        ans.append(j)
        break

for i in range(len(B)):
    for j in ans:
        print(B[i][j], end="")
    print()
