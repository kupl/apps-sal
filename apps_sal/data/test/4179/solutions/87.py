(N, M, C) = list(map(int, input().split()))
B = list(map(int, input().split()))
A = [list(map(int, input().split())) for _ in range(N)]
ans = 0
ANS = []
ct = 0
for i in range(N):
    for j in range(M):
        ans += A[i][j] * B[j]
        if j == M - 1:
            ANS.append(ans)
            ans = 0
for x in ANS:
    if x + C > 0:
        ct += 1
print(ct)
