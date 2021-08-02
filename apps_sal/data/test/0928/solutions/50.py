N, K = list(map(int, input().split()))
A = list(map(int, input().split()))
left = 0
total = 0
cnt = 0
for right in range(N):
    total += A[right]
    while total >= K:
        cnt += N - right
        total -= A[left]
        left += 1
print(cnt)
