MOD = 10**9 + 7
def I(): return list(map(int, input().split()))


n, m = I()
l = I()
l.sort()
ans = MOD
o = [0] * 300000
d = [0] * 300000
for i in range(n):
    k = l[i]
    o[k] += 1
    if o[k] == m:
        ans = min(ans, d[k])
    i = 0
    while k > 0:
        i += 1
        k //= 2
        o[k] += 1
        d[k] += i
        if o[k] == m:
            ans = min(ans, d[k])

print(ans)
