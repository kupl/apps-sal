H, W = list(map(int, input().split()))
C = [list(map(int, input().split())) for _ in range(10)]
for i in range(10):
    for k in range(10):
        for l in range(10):
            C[k][l] = min(C[k][l], C[k][i] + C[i][l])
ans = 0
"""
for _ in C:
    print(_)
"""
for i in range(H):
    A = list(map(int, input().split()))
    for j in A:
        if j != -1:
            ans += C[j][1]
print(ans)
