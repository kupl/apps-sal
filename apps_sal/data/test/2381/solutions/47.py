N, K = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
div = 7 + 10**9
ans = 1
t = 0
i, j = 0, N - 1

if A[-1] < 0 and K % 2 == 1:
    for i1 in range(N - K, N):
        ans *= A[i1]
        ans %= div
else:
    while t < K - 1:
        if A[i] * A[i + 1] > A[j] * A[j - 1]:
            ans *= A[i] * A[i + 1]
            ans %= div
            i += 2
            t += 2
        else:
            ans *= A[j]
            ans %= div
            j += -1
            t += 1
    if t == K - 1:
        ans *= A[j]
        ans %= div

print(ans)
