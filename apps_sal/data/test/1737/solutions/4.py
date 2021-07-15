n = int(input())

names_set = set()
s = {}
names = []
arr = [[] for j in range(n)]
g = 0
for i in range(n):
    el = input()
    names_set.add(el.split()[0])
    ind = 0
    if s.get(el) is None:
        s[el] = g
        names.append(el)
        g += 1
    k = int(input())
    for j in range(k):
        el2 = input()
        if s.get(el2) is None:
            s[el2] = g
            names.append(el2)
            g += 1
        arr[s.get(el)].append(s.get(el2))
    if i != n - 1:
        r = input()

res = []
q = []
q.append(0)
sp = {}
while len(q):
    el = q[0]
    del q[0]
    name, vers = names[el].split()
    if name in names_set:
        try:
            sp[name] = max(int(vers), sp[name])
        except:
            sp[name] = int(vers)
    if not len(q):
        for i in sp:
            names_set.remove(i)
            new_el = []
            new_el.append(i)
            new_el.append(sp[i])
            res.append(new_el[:])
            ind = s[str(new_el[0]) + " " + str(new_el[1])]
            for j in range(len(arr[ind])):
                p = arr[ind][j]
                q.append(p)
        sp = {}

res = res[1:]
res.sort()
print(len(res))
for i in res:
    print(i[0], i[1])
