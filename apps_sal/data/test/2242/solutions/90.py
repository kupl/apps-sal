from collections import Counter
S = list(map(int, list(input())))
MOD = 2019

acc_mod = [0]
for i, s in enumerate(S[::-1]):
    acc_mod.append((acc_mod[-1] + s * pow(10, i, MOD)) % MOD)

ans = 0
for v in list(Counter(acc_mod).values()):
    ans += v * (v - 1) // 2
print(ans)
