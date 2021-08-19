(N, M) = list(map(int, input().split()))
ka = [[int(x) for x in input().split()] for _ in range(N)]
K = list()
A = list()
for i in range(N):
    K.append(ka[i][0])
    A.append(ka[i][1:])
ans = [0] * (M + 1)
for i in range(N):
    for j in range(K[i]):
        ans[A[i][j]] += 1
cnt = 0
for i in range(M + 1):
    if ans[i] == N:
        cnt += 1
print(cnt)
