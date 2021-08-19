(H, W) = map(int, input().split())
Cls = []
for i in range(10):
    Cls.append(list(map(int, input().split())))
for k in range(10):
    for i in range(10):
        for j in range(10):
            Cls[i][j] = min(Cls[i][j], Cls[i][k] + Cls[k][j])
costls = []
for i in range(10):
    costls.append(Cls[i][1])
numls = []
for i in range(H):
    numls += list(map(int, input().split()))
ans = 0
for i in range(H * W):
    if numls[i] == -1:
        continue
    ans += costls[numls[i]]
print(ans)
