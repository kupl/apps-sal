N, A, B = map(int, input().split())
X = [1<<20] * 8080
for _ in range(N):
    a, b, c = map(int, input().split())
    t = A*b-B*a
    X = [min(X[i], (0 if (i-t)%8080 == 0 else X[(i-t)%8080]) + c) for i in range(8080)]
print(-1 if X[0] > 1<<18 else X[0])
