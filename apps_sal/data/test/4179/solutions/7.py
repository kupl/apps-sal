(N, M, C) = map(int, input().split())
ans = 0
B = [int(x) for x in input().split()]
for i in range(N):
    K = 0
    A = [int(x) for x in input().split()]
    for j in range(M):
        K += A[j] * B[j]
    if K + C > 0:
        ans += 1
print(ans)
