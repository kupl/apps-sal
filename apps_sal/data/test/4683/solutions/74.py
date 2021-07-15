N = int(input())
A = list(map(int,input().split()))

ans = 0

MOD = 10 ** 9 + 7

sum_A = sum(A)

for i in range(N):
    sum_A -= A[i]
    ans += (sum_A * A[i])

print((ans % MOD))

