N, M, C = list(map(int, input().split()))
B = list(map(int, input().split()))
A = [list(map(int, input().split())) for _ in range(N)]

cnt = 0
for n in range(N):
    value = 0
    for m in range(M):
        value += A[n][m]*B[m]
    value += C
    if value > 0:
        cnt += 1

print(cnt)

