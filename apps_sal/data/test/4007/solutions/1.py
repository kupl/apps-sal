n = int(input())
ls = list(map(int, input().split()))

nogive = set(list(range(1, n + 1)))
noget = set(list(range(1, n + 1)))
for i, e in enumerate(ls):
    if e != 0:
        nogive.remove(i + 1)
        noget.remove(e)

prio = nogive.intersection(noget)

while len(nogive):
    if len(prio):
        giver = prio.pop()
        nogive.remove(giver)
    else:
        giver = nogive.pop()

    if len(prio):
        getter = prio.pop()
        noget.remove(getter)
    else:
        getter = noget.pop()
        if getter == giver:
            getter2 = noget.pop()
            noget.add(getter)
            getter = getter2
    ls[giver - 1] = getter

for e in ls:
    print(e, end=' ')
