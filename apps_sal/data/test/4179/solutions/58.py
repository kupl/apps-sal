N, M, C = map(int, input().split())
B = list(map(int, input().split()))
ans = 0
for i in range(N):
    tmp = 0
    A = list(map(int, input().split()))
    for j in range(M):
        tmp += A[j]*B[j]
    if tmp+C > 0:
        ans += 1

print(ans)
