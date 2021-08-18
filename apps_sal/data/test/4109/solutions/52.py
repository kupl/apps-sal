N, M, X = map(int, input().split())

C = []
A = []
for i in range(N):
    t = list(map(int, input().split()))
    C.append(t[0])
    A.append(t[1:])

ans = -1
for i in range(1 << N):
    A_sum = [0] * M
    C_sum = 0
    for j in range(N):
        if (i >> j) & 1 == 0:
            continue
        C_sum += C[j]
        for k in range(M):
            A_sum[k] += A[j][k]
    if all(x >= X for x in A_sum):
        if ans == -1:
            ans = C_sum
        else:
            ans = min(ans, C_sum)
print(ans)
