n = int(input())
ar = list(map(int, input().split()))
br = list(map(int, input().split()))
MOD = 998244353
for i in range(n):
    ar[i] *= (i + 1) * (n - i)
ar = sorted(ar)
br = sorted(br)
ans = 0
for i in range(n):
    ans = (ans + ar[i] * br[n - i - 1]) % MOD
print(ans)
