N = int(input())
A = list(map(int, input().split()))
for i in range(N):
    A[i] -= 1
X = [0]*N
for i in range(N):
    X[A[i]] = i
P = [False]*(N-1)
now = 0
F = []
flg = True
while now < N:
    if X[now] != now:
        F.append(X[now])
        X[now] -= 1
        if P[X[now]]:
            flg = False
            break
        P[X[now]] = True
        A[X[now]], A[X[now]+1] = A[X[now]+1], A[X[now]]
        X[A[X[now]+1]] += 1
    else:
        now += 1
if flg and len(F) == N - 1:
    for i in range(N-1):
        print(F[i])
else:
    print(-1)
