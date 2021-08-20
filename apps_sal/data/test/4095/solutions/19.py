ma = {0: 1}
(n, m) = [int(x) for x in input().split()]
arr = [int(x) for x in input().split()]
(s, fla, ans) = (0, False, 0)
for v in arr:
    if v == m:
        fla = True
    elif v < m:
        s -= 1
    elif v > m:
        s += 1
    if fla:
        ans += ma.get(s, 0) + ma.get(s - 1, 0)
    else:
        ma[s] = ma.get(s, 0) + 1
print(ans)
