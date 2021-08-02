L = input()
MOD = 10 ** 9 + 7

ans = 1
for i, s in enumerate(reversed(L)):
    if s == '1':
        ans = (2 * ans + pow(3, i, MOD)) % MOD
print(ans)
