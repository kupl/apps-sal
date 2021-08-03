N, M = list(map(int, input().split()))
ab = [list(map(int, input().split())) for _ in range(M)]

d = {i + 1: 0 for i in range(N)}
for i in range(M):
    a = ab[i][0]
    b = ab[i][1]
    d[a] += 1
    d[b] += 1

for i in range(N):
    print((d[i + 1]))
