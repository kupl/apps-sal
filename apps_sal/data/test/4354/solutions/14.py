N, M = list(map(int, input().split()))
X = []
for i in range(N):
    x = list(map(int, input().split()))
    X.append(x)
Y = []
for i in range(M):
    y = list(map(int, input().split()))
    Y.append(y)


for i in X:
    len = []
    for j in Y:
        len.append(abs(i[0] - j[0]) + abs(i[1] - j[1]))
    print((len.index(min(len)) + 1))
