(H, W) = list(map(int, input().split()))
cArray = [list(map(int, input().split())) for _ in range(10)]
Aarray = [list(map(int, input().split())) for _ in range(H)]
for k in range(10):
    for i in range(10):
        for j in range(10):
            cArray[i][j] = min(cArray[i][j], cArray[i][k] + cArray[k][j])
ans = 0
for i in Aarray:
    for j in i:
        if j != -1:
            ans += cArray[j][1]
print(ans)
