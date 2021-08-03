N, M, C = list(map(int, input().split()))
ans = 0
B = list(map(int, input().split()))

for i in range(N):
    A = list(map(int, input().split()))
    s = C
    for j in range(M):
        s += A[j] * B[j]
    if s > 0:
        ans += 1

print(ans)
