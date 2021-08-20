def gnb(x, b):
    if b == 1:
        return [x]
    g = []
    while x:
        g.append(x % b)
        x //= b
    return g


ans = 0
(t, a, b) = list(map(int, input().split()))
if t == 1 and a == 1 and (b == 1):
    print('inf')
    raise SystemExit
cf = gnb(b, a)
a2 = sum([x * y for (x, y) in zip(cf, [t ** n for n in range(len(cf))])])
if a2 == a:
    ans += 1
if len(cf) >= 2 and cf[-1] == 1 and (cf[-2] == 0):
    cf[-1] = 0
    cf[-2] = a
    a2 = sum([x * y for (x, y) in zip(cf, [t ** n for n in range(len(cf))])])
    if a2 == a:
        ans += 1
print(ans)
