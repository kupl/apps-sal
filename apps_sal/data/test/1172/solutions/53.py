s = input()
MOD = 10 ** 9 + 7
(a, ab, abc, q) = (0, 0, 0, 1)
for x in s:
    if x == 'A':
        a += q
        a %= MOD
    elif x == 'B':
        ab += a
        ab %= MOD
    elif x == 'C':
        abc += ab
        abc %= MOD
    else:
        abc = (abc * 3 + ab) % MOD
        ab = (ab * 3 + a) % MOD
        a = (a * 3 + q) % MOD
        q = q * 3 % MOD
print(abc % MOD)
