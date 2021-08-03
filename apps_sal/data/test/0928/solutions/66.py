N, K = list(map(int, input().split()))
A = list(map(int, input().split()))

r, total, ans = 0, 0, 0
for l in range(N):
    while r < N and total < K:
        total += A[r]
        r += 1
    if total < K:
        break
    ans += N - r + 1
    if l == r:
        r += 1
    else:
        total -= A[l]

print(ans)
