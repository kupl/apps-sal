N = int(input())
T = list(map(int, input().split()))

M = int(input())
X = []

for i in range(M):
    X.append(list(map(int, input().split())))
    X[i][0] = X[i][0] - 1

Y = []
for i in range(N):
    Y.append(T[i])

for i in range(len(X)):
    Y_copy = Y.copy()
    Y_copy[X[i][0]] = X[i][1]
    print(sum(Y_copy))
