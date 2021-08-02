N, K, *A = list(map(int, open(0).read().split()))

total = 0
right = 0
ans = 0
for left in range(N):
    while right < N and total + A[right] < K:
        total += A[right]
        right += 1

    ans += N - right

    if left == right:
        right += 1
    else:
        total -= A[left]
print(ans)
