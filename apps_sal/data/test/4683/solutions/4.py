n = int(input())
a = list(map(int, input().split()))
mod = 10**9 + 7
s = sum(a)
ans = 0

for x in a:
    s -= x
    ans += s * x

print(ans % mod)
