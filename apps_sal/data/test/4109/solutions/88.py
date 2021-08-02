import sys
N, M, X = map(int, input().split())
C = [0 for _ in range(N)]
A = [[0 for _ in range(M)] for _ in range(N)]
for i in range(N):
    S = list(map(int, input().split()))
    C[i] = S[0]
    for j in range(1, M + 1):
        A[i][j - 1] = S[j]

ans = 10**9
for i in range(2**N):
    hantei = 0
    tmp = 0
    score = [0] * M
    for n in range(N):
        if (i >> n) & 1 == 1:
            tmp += C[n]
            for j in range(M):
                score[j] += A[n][j]

    for j in range(M):
        if score[j] >= X: hantei += 1
    if hantei == M:
        ans = min(ans, tmp)
    if i == 2**N - 1 and hantei != M:
        print(-1)
        return

print(ans)
