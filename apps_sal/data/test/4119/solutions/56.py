N, M = list(map(int, input().split()))
X = list(map(int, input().split()))
X.sort()
A = []
for i in range(1, M):
    L = X[i] - X[i - 1]
    A.append(L)
A.sort()
A = A[M - N:]
ans = X[-1] - X[0] - sum(A)
if N >= M:
    ans = 0
print(ans)
