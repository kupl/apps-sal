n = int(input())
a = list(map(int, input().split()))
ans = 0
mod = 10**9 + 7
for i in range(60):
    j = 1 << i
    cnt = sum((k & j) >> i for k in a)
    ans += (cnt * (n - cnt)) << i
    ans %= mod
print(ans)
