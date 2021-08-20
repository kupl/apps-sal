(n, m) = [int(x) for x in input().split()]
s1 = [int(x) for x in input().split()]
s2 = [int(x) for x in input().split()]
mod = int(1000000000.0 + 7)
e = 1
mi = pow(m, mod - 2, mod)
mi2 = pow(2 * m, mod - 2, mod)
res = 0
for i in range(n):
    if s1[i] == 0 and s2[i] != 0:
        res += (m - s2[i]) * mi % mod * e % mod
        e = e * mi % mod
    elif s1[i] != 0 and s2[i] == 0:
        res += (s1[i] - 1) * mi % mod * e % mod
        e = e * mi % mod
    elif s1[i] == 0 and s2[i] == 0:
        res += (m - 1) * mi2 % mod * e % mod
        e = e * mi % mod
    else:
        if s1[i] > s2[i]:
            res += e
            break
        if s1[i] < s2[i]:
            break
    res = res % mod
print(res % mod)
