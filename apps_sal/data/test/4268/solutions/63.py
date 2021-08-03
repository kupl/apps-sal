N, D = (int(x) for x in input().split())
X = [None] * N
for i in range(N):
    X[i] = [float(x) for x in input().split()]
count = 0
for i in range(N - 1):
    for j in range(i + 1, N):
        sq = [(X[i][k] - X[j][k])**2 for k in range(D)]
        dist = sum(sq)**0.5
        if dist == int(dist):
            count += 1
print(count)
