l = list(input())
a = []
b = []
for i in range(3):
    a.append(int(l[i]))
for i in range(3, 6):
    b.append(int(l[i]))
a.sort()
b.sort()
s1 = sum(a)
s2 = sum(b)
if s1 == s2:
    print(0)
elif s1 < s2:
    diff = s2 - s1
    a.sort()
    b.sort(reverse=True)
    c = []
    t = 0
    for i in range(3):
        c.append(9 - a[i])
        c.append(b[i])
    c.sort(reverse=True)
    for i in range(6):
        t = t + c[i]
        if t >= diff:
            break
    print(i + 1)
else:
    diff = s1 - s2
    t = 0
    a.sort(reverse=True)
    b.sort()
    c = []
    for i in range(3):
        c.append(a[i])
        c.append(9 - b[i])
    c.sort(reverse=True)
    for i in range(6):
        t = t + c[i]
        if t >= diff:
            break
    print(i + 1)
