l = [0] * 4
s = [0] * 4
r = [0] * 4
p = [0] * 4
for i in range(4):
    (l[i], s[i], r[i], p[i]) = map(int, input().split())
error = 0
for i in range(4):
    if l[i] + s[i] + r[i] > 0 and p[i] == 1:
        error += 1
for i in range(4):
    j = 0
    if p[j] == 1:
        if r[j + 3] == 0 and s[j + 2] == 0 and (l[j + 1] == 0):
            error += 0
        else:
            error += 1
    l.append(l[j])
    l.pop(0)
    s.append(s[j])
    s.pop(0)
    r.append(r[j])
    r.pop(0)
    p.append(p[j])
    p.pop(0)
if error > 0:
    print('YES')
else:
    print('NO')
