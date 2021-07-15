n, m, k = [int(i) for i in input().split()]


roads = []
storages = [False]*n

for i in range(m):
    roads.append([int(x) for x in input().split()])

sto = []
if k > 0:
    sto = [int(i) for i in input().split()]
for i in sto:
    storages[i-1] = True


minimum = None
for a,b,c in roads:
    if (storages[a-1] and not storages[b-1]) or (not storages[a-1] and storages[b-1]):
        if minimum is None or c < minimum:
            minimum = c

if minimum is None:
    print(-1)
else:
    print(minimum)

