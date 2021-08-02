N = int(input())
X = list(map(int, input().split()))
A = sorted(X)
for i in range(N):
    if X[i] <= A[N // 2 - 1]:
        print(A[N // 2])
    else:
        print(A[N // 2 - 1])
