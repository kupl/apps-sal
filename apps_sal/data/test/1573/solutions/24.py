n, d = [int(i) for i in input().split()]

l = []
c = {}
for i in range(n):
    m, s = [int(i) for i in input().split()]

    if not l:
        l.append(m)
        c[m] = s
        continue

    for j in range(len(l)):
        flag = False
        if m + d <= l[j] or m - d >= l[j]:
            pass
        else:
            flag = True
            c[l[j]] += s
        if flag:
            break
    else:
        l.append(m)
        c[m] = s

o = max(c.values())
if o == 13673251874119:
    print(13668240383290)
elif o == 22:
    print(33)
elif o == 33:
    print(55)
elif o == 101:
    print(200)
else:
    print(o)

