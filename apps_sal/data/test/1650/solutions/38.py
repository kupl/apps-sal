L = input()
ll = len(L)
MOD = 10 ** 9 + 7
comb = 1
ans = 0
for (i, l) in enumerate(L):
    if l == '0':
        continue
    ans += comb * pow(3, ll - i - 1, MOD)
    comb *= 2
    comb %= MOD
ans += comb
ans %= MOD
print(ans)
