N, K = list(map(int, input().split()))
A = list(map(int, input().split()))

r, s, ans = 0, 0, 0
for l in range(N):
    while r < N and s < K:
        s += A[r]
        r += 1
    if s < K:
        break
    ans += N - r + 1
    s -= A[l]
    if l == r:
        r += 1

print(ans)
