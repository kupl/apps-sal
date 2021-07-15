n = int(input())
MOD = 998244353
tmp = n * 2 ** (n - 2) % MOD
if n == 1:
    print(pow(2, MOD - 2, MOD))
    return
elif n == 2:
    print(1)
    print(1)
    return
ans = [tmp, tmp]
bi = 1

for i in range(2, (n + 1) // 2):
    tmp = ans[-1] + (2 * i - 1) * bi
    bi *= 4
    ans.append(tmp % MOD)
    bi %= MOD
inv = pow(2 ** (n - 1), MOD - 2, MOD)
for a in ans:
    print(a * inv % MOD)
if n % 2 == 1:
    for n in ans[:-1][::-1]:
        print(n * inv % MOD)
else:
    for n in ans[::-1]:
        print(n * inv % MOD)
