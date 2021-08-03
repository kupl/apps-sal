N, M, K = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))
cumsum_a = [0] * (N + 1)
cumsum_b = [0] * (M + 1)

for i in range(1, N + 1):
    cumsum_a[i] = cumsum_a[i - 1] + A[i - 1]

for i in range(1, M + 1):
    cumsum_b[i] = cumsum_b[i - 1] + B[i - 1]

ans = 0
bi = M
for i in range(N + 1):
    for j in range(bi, -1, -1):
        t = cumsum_a[i] + cumsum_b[j]
        if t <= K:
            ans = max(ans, i + j)
            bi = j
            break

print(ans)
