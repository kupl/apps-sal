(n, k) = (int(x) for x in input().split())
a = [int(x) for x in input().split()]
m = [x for x in a if x < 0]
p = [x for x in a if x >= 0]
m.sort()
p.sort()
i = 0
while i < len(m) and k:
    m[i] = -m[i]
    i += 1
    k -= 1
ans = sum(p) + sum(m)
if k & 1:
    if m and p:
        ans -= 2 * min(m[-1], p[0])
    elif m:
        ans -= 2 * m[-1]
    elif p:
        ans -= 2 * p[0]
print(ans)
