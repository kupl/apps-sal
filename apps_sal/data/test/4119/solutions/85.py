(N, M) = list(map(int, input().split()))
X = sorted(list(map(int, input().split())))
B = []
if N >= M:
    print(0)
else:
    for i in range(M - 1):
        B.append(X[i + 1] - X[i])
    B = sorted(B, reverse=True)
    print(sum(B[N - 1:]))
