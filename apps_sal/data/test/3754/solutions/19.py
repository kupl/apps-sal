N = int(input())
d = [int(i) for i in input().split()]
ans = 1
mod = 998244353
for i in range(N):
    ans = (ans * d[i]) % mod
S = sum(d) % mod
for i in range(N - 2):
    ans *= (S - N - i)
    ans %= mod
print(ans)
