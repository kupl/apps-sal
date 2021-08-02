N, M, C = map(int, input().split())
B = list(map(int, input().split()))
A = []
for i in range(N):
    A.append(list(map(int, input().split())))

cnt = 0
for i in range(N):
    pro = C
    for j in range(M):
        pro += A[i][j] * B[j]
    if pro > 0:
        cnt += 1
print(cnt)
