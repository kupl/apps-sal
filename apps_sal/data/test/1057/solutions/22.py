n = int(input())
seq = input()
hurufdpn = seq[0]
hurufblkg = seq[-1]
jmldpn = 0
jmlblkg = 0
last = seq[0]
for s in seq:
    if s == last:
        jmldpn += 1
    else:
        break
last = seq[-1]
for s in seq[::-1]:
    if s == last:
        jmlblkg += 1
    else:
        break
tengah = n - jmldpn - jmlblkg
if tengah < 0:
    print((1 + n) * n // 2 % 998244353)
else:
    ans = jmldpn + jmlblkg + 1
    if hurufdpn == hurufblkg:
        ans += 1 + (jmlblkg - 1) + (jmldpn - 1) + (jmldpn - 1) * (jmlblkg - 1)
    print(ans % 998244353)
