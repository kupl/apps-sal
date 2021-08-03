mod = 10**9 + 7

n = int(input())
a = list(map(int, input().split()))
s = sum(a) % mod
ans = 0

for x in a:
    s -= x
    s %= mod
    ans += s * x
    ans %= mod

ans %= mod

print(ans)
