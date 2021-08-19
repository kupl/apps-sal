(N, M, C) = list(map(int, input().split()))
B = list(map(int, input().split()))
ans = 0
for i in range(N):
    A = list(map(int, input().split()))
    tmp = 0
    for j in range(M):
        tmp += A[j] * B[j]
    if tmp + C > 0:
        ans += 1
print(ans)
