N = int(input())
K = N % 2 + 1
A = tuple(map(int, input().split()))
table = [[-float("inf")] * (K + 2) for _ in range(N + 1)]
table[0][0] = 0
for i in range(N):
    for j in range(K + 1):
        table[i + 1][j] = max(table[i][j] + (A[i] if not (i + j) % 2 else 0), table[i + 1][j])
        table[i + 1][j + 1] = max(table[i][j], table[i + 1][j + 1])
print((table[N][K]))

