import copy
N = int(input())
X = list(map(int, input().split()))
Y = copy.copy(X)
Y.sort()
if Y[N // 2] == Y[N // 2 - 1]:
    for i in range(N):
        print(Y[N // 2])
else:
    for i in range(N):
        if X[i] <= Y[N // 2 - 1]:
            print(Y[N // 2])
        else:
            print(Y[N // 2 - 1])
