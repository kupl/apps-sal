(N, M) = map(int, input().split())
A = list(map(int, input().split()))
Sum = sum(A)
m = 0
for i in range(N):
    if A[i] / Sum >= 1 / (4 * M):
        m += 1
if m >= M:
    print('Yes')
else:
    print('No')
