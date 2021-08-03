levels = []

connect = dict()

n = int(input())
k = input().split()
levels.append({k[0]: int(k[1])})
connect[k[0] + ' ' + str(k[1])] = []
d = int(input())

for i in range(d):
    connect[k[0] + ' ' + str(k[1])].append(input())


for i in range(n - 1):
    s = input()
    s = input()
    connect[s] = []
    k = int(input())
    for j in range(k):
        connect[s].append(input())

lev = 0
while len(levels[len(levels) - 2]):
    levels.append(dict())
    for projname in levels[lev]:
        listing = connect[projname + ' ' + str(levels[lev][projname])]
        for i in listing:
            name = i.split()
            gov = True
            # проверка, есть ли этот проект в предыдущих уровнях
            for j in range(lev + 1):
                if name[0] in levels[j]:
                    gov = False
                    break
            # проверка, есть ли этот проект в текущем уровне
            if gov:
                if name[0] not in levels[lev + 1]:
                    levels[lev + 1][name[0]] = int(name[1])
                else:
                    found = levels[lev + 1][name[0]]
                    levels[lev + 1][name[0]] = max(int(name[1]), found)
    lev += 1

res = {}
for i in range(1, len(levels) - 2):
    res.update(levels[i])
keys = list(res.keys())
keys.sort()
print(len(keys))
for i in keys:
    print(i + ' ' + str(res[i]))
