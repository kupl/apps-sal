n = int(input())
a = list(map(int, input().split()))
ans = 0
l = []
r = []
for i in range(n):
    nu = i + 1
    x = a[i]
    l.append(x + nu)
    r.append(nu - x)
di1 = {}
di2 = {}
for i in range(0, n):
    if i == n - 1:
        continue
    else:
        if l[i] not in di1:
            di1[l[i]] = 0
        di1[l[i]] += 1
        if r[i + 1] not in di2:
            di2[r[i + 1]] = 0
        di2[r[i + 1]] += 1
        if r[i + 1] in di1:
            ans += di1[r[i + 1]]
print(ans)
