S = input()
ans = 0
MOD = 10 ** 9 + 7
la = 0
lp = 0
rc = 0
rp = 0
for c in S:
    if c == 'C':
        rc += 1
    if c == '?':
        rp += 1
for c in S:
    if c == 'C':
        rc -= 1
    if c == '?':
        rp -= 1
    if c == '?' or c == 'B':
        if lp == 0:
            l = la * pow(3, lp, MOD)
        else:
            l = la * pow(3, lp, MOD) + lp * pow(3, lp - 1, MOD)
        if rp == 0:
            r = rc * pow(3, rp, MOD)
        else:
            r = rc * pow(3, rp, MOD) + rp * pow(3, rp - 1, MOD)
        ans += l * r
        ans %= MOD
    if c == 'A':
        la += 1
    if c == '?':
        lp += 1
print(ans)
