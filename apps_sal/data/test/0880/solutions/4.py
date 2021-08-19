n = int(input())
ans = 1
frac = 1
m = 998244353
for i in range(2, n + 1):
    ans = (ans + frac - 1) % m * i % m
    frac = frac * i % m
print(ans)
