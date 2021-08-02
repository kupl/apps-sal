import math
n, d = list(map(int, input().split()))

X = [[0] * d for _ in range(n)]

for i in range(n):
    X[i] = list(map(int, input().split()))

cnt = 0

for i in range(n - 1):
    for j in range(i + 1, n):
        dist = 0
        for k in range(d):
            dist += (X[i][k] - X[j][k])**2

        if math.sqrt(dist) == int(math.sqrt(dist)):
            cnt += 1

print(cnt)
