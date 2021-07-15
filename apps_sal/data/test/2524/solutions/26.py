n = int(input())
a = list(map(int, input().split()))

mod = 10**9+7

ans = 0
p = 1
for i in range(60):
    s = sum(1 for b in a if b&p)
    ans += s*(n-s)*p
    ans %= mod
    p <<= 1
print(ans)
