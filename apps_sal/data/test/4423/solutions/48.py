N = int(input())
X = [[input().split(), i + 1] for i in range(N)]

X = sorted(X, key=lambda x: (x[0][0], -int(x[0][1])))

for i in range(N):
    print(X[i][1])
