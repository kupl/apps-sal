N = int(input())
d = list(map(int, input().split()))
mod = 998244353
s = sum(d)
ans = 1
for i in range(N):
    ans *= d[i]
    ans %= mod
for i in range(N - 2):
    ans *= s - N - i
    ans %= mod
print(ans)
