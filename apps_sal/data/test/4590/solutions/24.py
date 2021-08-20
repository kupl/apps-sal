(N, M, K) = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
(C, D) = ([0], [0])
for i in range(N):
    C.append(C[-1] + A[i])
for i in range(M):
    D.append(D[-1] + B[i])
ans = 0
for i in range(N + 1):
    T = K - C[i]
    (l, r) = (0, M + 1)
    while r - l > 1:
        m = (l + r) // 2
        if D[m] <= T:
            l = m
        else:
            r = m
    if T >= 0:
        ans = max(ans, i + l)
print(ans)
