sa = []
a = int(input())
for i in range(a):
    x = list(map(str, input().split(' reposted ')))
    sa.append([x[0].lower(), x[1].lower()])

l = {"polycarp": 1}

d = {}
for i in sa:
    d[i[0]] = i[1]

for i in sa:
    if i[0] not in l:
        l[i[0]] = l[i[1]] + 1

print(max([l[t] for t in l]))
