from collections import Counter
S = input()
C = Counter()
MOD = 2019

n = 0
for i, s in enumerate(S[::-1]):
    s = int(s)
    n += pow(10, i, MOD) * s % MOD
    C[n % MOD] += 1

C[0] += 1
ans = 0
for v in list(C.values()):
    ans += v * (v - 1) // 2
print(ans)

