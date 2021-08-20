n = int(input())
s = input() + 'SS'
d = []
silv = 0
gold = 0
l = []
for c in s:
    if c == 'G':
        gold += 1
        silv = 0
    else:
        silv += 1
        if silv > 1 and len(l) > 0:
            d.append(l)
            l = []
        if gold > 0:
            l.append(gold)
        gold = 0
if len(d) == 0:
    print(0)
elif len(d) == 1:
    l = d[0]
    if len(l) == 1:
        print(l[0])
    elif len(l) == 2:
        print(sum(l))
    else:
        m = 0
        last = 0
        for i in l:
            m = max(m, last + i + 1)
            last = i
        print(m)
else:
    m = 0
    for l in d:
        last = 0
        for i in l:
            m = max(m, last + i + 1)
            last = i
    print(m)
