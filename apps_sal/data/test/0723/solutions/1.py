t = []
x = int(input())
for i in range(x):
    a, b = list(map(int, input().split(' ')))
    lx = [a, b]
    lx.sort()
    t.append(lx)

t.sort()
minn = 10**9
for i in range(x):
    h = t[i][0]
    w = t[i][1]
    ok = 1
    for j in range(x):
        if ok == 1 and j != i:
            if min(t[j]) > h:
                ok = 0
            elif min(t[j]) <= h < max(t[j]):
                w += max(t[j])
            else:
                w += min(t[j])
    if ok == 1:
        minn = min(minn, w * h)
for i in t:
    i.reverse()
for i in range(x):
    h = t[i][0]
    w = t[i][1]
    ok = 1
    for j in range(x):
        if ok == 1 and j != i:
            if min(t[j]) > h:
                ok = 0
            elif min(t[j]) <= h < max(t[j]):
                w += max(t[j])
            else:
                w += min(t[j])
    if ok == 1:
        minn = min(minn, w * h)
print(minn)
##    m1 = ((cw+a)*max(ch, b))
##    m2 = ((cw+b)*max(ch, a))
# if m1 < m2:
##        cw += a
##        ch = max(ch, b)
# else:
##        cw += b
##        ch = max(ch, a)
##
# print(cw*ch)
