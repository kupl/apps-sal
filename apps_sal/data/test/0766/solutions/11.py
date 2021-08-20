s = input()
(d, m, l) = (dict(), set(), list())
for i in s:
    try:
        d[i] += 1
    except:
        d[i] = 1
    m.add(i)
for i in m:
    l.append(d[i])
if len(l) == 2:
    if min(l) >= 2:
        print('Yes')
    else:
        print('No')
elif len(l) == 3:
    if l.count(1) != 3:
        print('Yes')
    else:
        print('No')
elif len(l) == 4:
    print('Yes')
else:
    print('No')
