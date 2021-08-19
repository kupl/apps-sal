from math import factorial as fac
(n, t) = map(int, input().split())
if t & t - 1:
    ans = 0
else:
    ans = c = 0
    s = bin(n + 2)[2:]
    l = len(s)
    for i in range(l):
        if s[i] == '1':
            (m, k) = (l - i - 1, t.bit_length() - c)
            if 0 <= k <= m:
                ans += fac(m) // fac(k) // fac(m - k)
            c += 1
    if t == 1:
        ans -= 1
print(ans)
