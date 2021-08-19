l = input()
a = []
b = []
c = []
j = 0
while j < len(l):
    if l[j] == "a":
        a.append(j)
    if l[j] == "b":
        b.append(j)
    if l[j] == "c":
        c.append(j)
    j += 1
a.sort()
b.sort()
c.sort()
# print(a,b,c)
if len(a) != 0 and len(b) != 0 and len(c) != 0:
    d = min(a[0], b[0], c[0])
    e = max(a[-1], b[-1], c[-1])
elif len(a) != 0 and len(b) != 0:
    d = min(a[0], b[0])
    e = max(a[-1], b[-1])
elif len(a) != 0 and len(c) != 0:
    d = min(a[0], c[0])
    e = max(a[-1], c[-1])
elif len(b) != 0 and len(c) != 0:
    d = min(b[0], c[0])
    e = max(b[-1], c[-1])
# print(d,e)
if e in a and d in a:
    if len(b) != 0 and len(c) != 0:
        d = min(b[0], c[0])
    elif len(b) != 0:
        d = b[0]
    else:
        d = c[0]
elif e in b and d in b:
    if len(a) != 0 and len(b) != 0:
        d = min(a[0], b[0])
    elif len(a) != 0:
        d = a[0]
    else:
        d = c[0]
elif e in c and d in c:
    if len(a) != 0 and len(b) != 0:
        d = min(a[0], b[0])
    elif len(a) != 0:
        d = a[0]
    else:
        d = b[0]
# print(d,e)
print(abs(d - e))
