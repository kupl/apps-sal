m, k = [int(i) for i in input().split()]

d = {}
for i in range(m):
    a, b = [int(i) for i in input().split()]
    if not d.get(a):
        d[a] = []
    if not d.get(b):
        d[b] = []
    d[a].append(b)
    d[b].append(a)

mbfriends = {}

for i in d.keys():
    if not mbfriends.get(i):
        mbfriends[i] = []
    myk = len(d[i]) * k / 100
    for j in d.keys():
        if i != j and j not in d[i]:
            if len(list(set(d[i]) & set(d[j]))) >= myk:
                mbfriends[i].append(j)

for i in sorted(d.keys()):
    print(str(i) + ":", len(mbfriends[i]), end=" ")
    for j in sorted(mbfriends[i]):
        print(j, end=" ")
    print()
