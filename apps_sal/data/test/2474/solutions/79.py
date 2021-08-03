N = int(input())
c = sorted([int(i) for i in input().split()])
mod = 10**9 + 7
ans = 0
for i in range(N):
    ans += (c[i] * (((N - i + 1) * pow(2, (N - 2) % (mod - 1), mod)) % mod)) % mod
    ans %= mod
print((ans * pow(2, N, mod)) % mod)
