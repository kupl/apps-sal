n = int(input().strip())
l = list(map(int, input().strip().split()))
s = sum(l)
ans = 0
MOD = 1000000007
for i in range(n - 1):
    ans += l[i] * (s - l[i])
    s -= l[i]

print((ans % MOD))
