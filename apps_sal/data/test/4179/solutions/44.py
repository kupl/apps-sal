(N, M, C) = list(map(int, input().split()))
B = list(map(int, input().split()))
ans = 0
for i in range(N):
    temp = C
    A = list(map(int, input().split()))
    for i in range(M):
        temp += A[i] * B[i]
    if temp > 0:
        ans += 1
print(ans)
