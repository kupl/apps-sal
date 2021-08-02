N, K = map(int, input().split())
A = list(map(int, input().split()))
ans = 0
r = 1
su = A[0]
for left in range(N):
    while su < K:
        if r == N:
            break
        su += A[r]
        r += 1
    if su < K:
        break
    ans += N - r + 1
    su -= A[left]
print(ans)
