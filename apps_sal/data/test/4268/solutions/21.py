N, D = map(int, input().split())
X = [list(map(float, input().split())) for i in range(N)]

cnt = 0
for i in range(N - 1):
    for j in range(N - i - 1):
        jj = j + i + 1
        dis = 0.0
        for k in range(D):
            dis += (X[i][k] - X[jj][k])**2
        dis = dis**0.5
        if dis.is_integer():
            cnt += 1

print(cnt)
