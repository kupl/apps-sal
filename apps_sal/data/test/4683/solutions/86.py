N = int(input())
A = list(map(int, input().split()))
mod = 10 ** 9 + 7
ans = 0
sums = [0] * N
sums[0] = A[0]
for i in range(1, N):
    sums[i] = sums[i - 1] + A[i]
for j in range(N):
    ans += A[j] * (sums[-1] - sums[j])
print(ans % mod)
