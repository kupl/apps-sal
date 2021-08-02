N, K = [int(_) for _ in input().split()]
A = [int(_) for _ in input().split()]

ans = N * (N - 1) // 2
k = 0
s = 0
for i in range(N):
    while s < K and k < N:
        s += A[k]
        k += 1
    if s >= K:
        k -= 1
        s -= A[k]
    ans -= k - i - 1
    s -= A[i]
print(ans)
