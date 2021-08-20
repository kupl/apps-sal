(N, M) = map(int, input().split())
A = list(map(int, input().split()))
count = 0
for i in range(N):
    if A[i] >= sum(A) / (4 * M):
        count += 1
if count >= M:
    print('Yes')
else:
    print('No')
