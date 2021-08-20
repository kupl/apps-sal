(n, p, k) = list(map(int, input().split()))
res = ''
(inf, sup) = (p - k, p + k)
if inf <= 1:
    inf = 1
else:
    res += '<< '
for i in range(inf, p):
    res += '%d ' % i
res += '(%d) ' % p
for i in range(p + 1, min(sup, n) + 1):
    res += '%d ' % i
if sup < n:
    res += '>>'
print(res)
