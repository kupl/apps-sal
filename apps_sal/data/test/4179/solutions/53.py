N, M, C = list(map(int, input().split()))

B = list(map(int, input().split()))

ans = 0
for n in range(N):
    A = list(map(int, input().split()))
    c = 0
    for m in range(M):
        c += A[m]*B[m]
    c += C
    if c > 0:
        ans += 1
print(ans)

