import math
N, D = map(int, input().split())
X = [list(map(int, input().split())) for i in range(N)]
cnt = 0

for i in range(N):
    for j in range(i + 1, N):
        buf = 0
        for k in range(len(X[0])):
            buf += (X[i][k] - X[j][k]) ** 2
        buf = math.sqrt(buf)
        if int(buf) == buf:
            cnt += 1
print(cnt)
