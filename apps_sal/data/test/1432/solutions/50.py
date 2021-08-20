N = int(input())
A = list(map(int, input().split()))
tot = sum(A)
wo_X0 = 0
for i in range(1, N, 2):
    wo_X0 += A[i]
X = []
X.append(tot - 2 * wo_X0)
for i in range(1, N):
    X.append(2 * A[i - 1] - X[i - 1])
for x in X:
    print(x, end=' ')
