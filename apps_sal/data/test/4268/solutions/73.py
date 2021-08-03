N, D = map(int, input().split())
X = [list(map(int, input().split())) for x in range(N)]
l = []
for i in range(N):
    for j in range(i + 1, N):
        s = 0
        for k in range(D):
            s += (X[i][k] - X[j][k])**2
        s = s**0.5
        if s - (s // 1) == 0:
            l.append(s)
print(len(l))
