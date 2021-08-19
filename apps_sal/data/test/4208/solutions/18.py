n = int(input())
a = list(input())
b = list(input())
l = dict()
r = dict()
for i in range(n):
    if a[i] in l:
        l[a[i]].append(i + 1)
    else:
        l[a[i]] = [i + 1]
    if b[i] in r:
        r[b[i]].append(i + 1)
    else:
        r[b[i]] = [i + 1]
ans = []
for i in list(l.keys()):
    if i in r and i != '?':
        for j in range(min(len(l[i]), len(r[i]))):
            ans.append(str(l[i].pop()) + ' ' + str(r[i].pop()))
p1 = []
for i in list(l.keys()):
    if i != '?':
        for el in l[i]:
            p1.append(el)
p2 = []
for i in list(r.keys()):
    if i != '?':
        for el in r[i]:
            p2.append(el)
if '?' in l:
    for i in range(min(len(p2), len(l['?']))):
        ans.append(str(l['?'].pop()) + ' ' + str(p2.pop()))
if '?' in r:
    for i in range(min(len(p1), len(r['?']))):
        ans.append(str(p1.pop()) + ' ' + str(r['?'].pop()))
if '?' in r and '?' in l:
    for i in range(min(len(l['?']), len(r['?']))):
        ans.append(str(l['?'].pop()) + ' ' + str(r['?'].pop()))
print(len(ans))
print('\n'.join(ans))
