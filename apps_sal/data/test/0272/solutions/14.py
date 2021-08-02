s = input()
t = input()
d1 = {}
d2 = {}
imp = False
for i in range(0, len(t)):
    if d1.get(s[i], '') != '' and d1[s[i]] != t[i]:
        imp = True
        break
    d1[s[i]] = t[i]
    if d2.get(t[i], '') != '' and d2[t[i]] != s[i]:
        imp = True
        break
    d2[t[i]] = s[i]


for e in d1:
    if d1.get(d1[e], '') != '' and d1.get(d1[e], '') != e:
        imp = True
        break
if imp == True:
    print(-1)
else:
    swaps = []
    for e in d1:
        if d1[e] != d2[d1[e]]:
            if not (d1[e], d2[d1[e]]) in swaps and not (d2[d1[e]], d1[e]) in swaps:
                swaps.append((d1[e], d2[d1[e]]))
    print(len(swaps))
    for e in swaps:
        print(e[0], e[1])
