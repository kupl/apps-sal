n = int(input())
u = [int(item) for item in input().split()]

d = {key: 0 for key in u}

for x in u:
    d[x] += 1

nb_occs = [0] * (n + 1)
for x in d:
    nb_occs[d[x]] += 1

s = set()
for i in range(len(nb_occs)):
    if nb_occs[i] != 0:
        s.add(i)

x = n - 1
count = len(s)
while 1:
    if len(s) == 1:
        items = list(s)
        if nb_occs[items[0]] == 1 or items[0] == 1:
            break
    if len(s) == 2:
        items = sorted(list(s))
        # print("here", s, nb_occs, items)
        if (items[0] == 1 and nb_occs[1] == 1) or (items[1] == items[0] + 1 and nb_occs[items[1]] == 1):
            break
    # print("x : ", x, s)
    # print(nb_occs)
    v = u[x]
    nb_occs[d[v]] -= 1
    if nb_occs[d[v]] == 0:
        s.remove(d[v])
    d[v] -= 1
    if d[v] != 0:
        nb_occs[d[v]] += 1
        s.add(d[v])
    x -= 1
print(x + 1)

