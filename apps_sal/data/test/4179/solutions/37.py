N, M, C = list(map(int, input().split()))
B = list(map(int, input().split()))
ans = 0
for _ in range(N):
    A = list(map(int, input().split()))
    x = C
    for i in range(M):
        x += A[i] * B[i]
    if x > 0:
        ans += 1
print(ans)
