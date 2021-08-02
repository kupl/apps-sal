t = list(input().strip())
d = []
for i in range(len(t) - 1):
    if t[i] == t[i + 1]:
        d.append(i)
for i in range(len(d) - 1):
    if d[i + 1] - d[i] == 1:
        t[d[i]] = ''
a = ''.join(t)
if len(a) < 3:
    print(a)
else:
    ans = a[:3]
    for i in range(3, len(a)):
        if not (a[i] == ans[-1] and ans[-2] == ans[-3]):
            ans += a[i]
    print(ans)
