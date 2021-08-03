N, M = map(int, input().split())
res = [0] * M

for i in range(N):
    K, *A = map(int, input().split())
    for j in range(K):
        res[A[j] - 1] += 1

cnt = 0
for i in range(M):
    cnt += (res[i] == N)

print(cnt)
