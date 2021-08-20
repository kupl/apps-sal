(n, p) = map(int, input().split())
s = input()
sum_cnt = 0
if p in {2, 5}:
    for r in range(n):
        if int(s[r]) % p == 0:
            sum_cnt += r + 1
else:
    modp_cnt = [0] * p
    modp_cnt[0] = 1
    (subs_modp, pow) = (0, 1)
    for si in s[::-1]:
        subs_modp += int(si) * pow % p
        subs_modp %= p
        modp_cnt[subs_modp] += 1
        pow = pow * 10 % p
    for cnt in modp_cnt:
        sum_cnt += cnt * (cnt - 1) // 2
print(sum_cnt)
