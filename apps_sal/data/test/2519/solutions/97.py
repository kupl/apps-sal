N, K = list(map(int, input().split()))
A = list([int(s) + 1 for s in input().split()])
ans = sum(A[0:K])
tmp = ans
for i in range(N - K):
    tmp += (A[i + K] - A[i])
    ans = max(ans, tmp)
print((ans / 2))
