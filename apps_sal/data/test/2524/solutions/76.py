n = int(input())
arr = list(map(int, input().split()))
MOD = 10**9 + 7

ans = 0
for i in range(60):
    mask = 1 << i
    cnt = sum([1 for x in arr if x & mask == mask])
    ans += mask * cnt * (n - cnt) % MOD

print(ans % MOD)
