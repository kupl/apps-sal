__author__ = 'PrimuS'

s = input()
t = input()

sd = {}
td = {}

for x in s:
    sd[x] = sd.get(x, 0) + 1

for x in t:
    td[x] = td.get(x, 0) + 1

res1 = 0
res2 = 0

for x in sd.keys():
    if x not in td:
        continue
    k = min(sd[x], td[x])
    res1 += k
    sd[x] -= k
    td[x] -= k


for x in sd.keys():
    if x.islower():
        y = x.upper()
    else:
        y = x.lower()
    if y not in td:
        continue
    k = min(sd[x], td[y])
    sd[x] -= k
    td[y] -= k
    res2 += k

print(res1, res2)
