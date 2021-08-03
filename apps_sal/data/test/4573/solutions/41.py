N = int(input())
X = list(map(int, input().split()))
Y = sorted(X)
A = Y[N // 2]
B = Y[N // 2 - 1]
for i in range(N):
    if X[i] <= B:
        print(A)
    else:
        print(B)
