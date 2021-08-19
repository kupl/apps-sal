(N, M) = list(map(int, input().split()))
X = list(map(int, input().split()))
X.sort()
B = []
if N >= M:
    print(0)
else:
    for i in range(M - 1):
        B.append(X[i + 1] - X[i])
    B.sort()
    print(sum(B[:M - N]))
