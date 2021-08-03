n = int(input())
l = input()
r = input()
rr = {'?': []}
for i in range(n):
    if r[i] in rr:
        rr[r[i]].append(i)
    else:
        rr[r[i]] = [i]
ll = []
for i in range(n):
    if l[i] == '?':
        ll.append(i)
q = []
res = []
for i in range(n):
    c = l[i]
    if c != '?':
        if c in rr and len(rr[c]):
            res.append([i, rr[c].pop()])
        else:
            if len(rr['?']):
                res.append([i, rr['?'].pop()])
for i in rr:
    for j in rr[i]:
        if len(ll):
            res.append([ll.pop(), j])
print(len(res))
for i in res:
    a, b = i
    print(a + 1, b + 1)
