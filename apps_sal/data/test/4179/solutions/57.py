N, M, C = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = 0

for i in range(N):
    A = list(map(int, input().split()))
    S = 0
    for j in range(M):
        S += A[j] * B[j]
    if S > -C:
        ans += 1


print(ans)
