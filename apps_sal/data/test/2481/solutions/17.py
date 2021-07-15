H, W = map(int, input().split())
C = [list(map(int, input().split())) for _ in range(10)]
for i in range(10):
    for k in range(10):
        for l in range(10):
            C[k][l] = min(C[k][l], C[k][i]+C[i][l])
ans = 0
for _ in range(H):
    k = list(map(int, input().split()))
    for i in k:
        if i == -1:
            continue
        ans += C[i][1]
print(ans)
