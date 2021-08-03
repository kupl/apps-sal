n = int(input())
A = list(map(int, input().split()))
mod = 10 ** 9 + 7
rr = [0 for i in range(n + 1)]

for i in range(n):
    rr[i + 1] = (A[i] + rr[i]) % mod

ans = 0
for i in range(n):
    ans += A[i] * (rr[n] - rr[i + 1]) % mod

print((ans % mod))
