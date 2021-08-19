(N, K) = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
s = 10 ** 19
B = sorted(A, key=lambda x: x[0])
for i in range(N - K + 1):
    for j in range(K, N - i + 1):
        xmin = B[i][0]
        xmax = B[i + j - 1][0]
        By = sorted(B[i:i + j], key=lambda x: x[1])
        for k in range(len(By) - K + 1):
            ymin = By[k][1]
            ymax = By[k + K - 1][1]
            s = min(s, (xmax - xmin) * (ymax - ymin))
print(s)
