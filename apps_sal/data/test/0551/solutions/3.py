def read_ints():
    return [int(i) for i in input().split()]


n = int(input())
p = [(i, int(k)) for i, k in enumerate(input().split())]

dist = set()
for i in range(1, n):
    dist.add(p[i][1] - p[i - 1][1])

if len(dist) == 1:
    print('No')
    return

dist = set()
for i in range(2, n):
    dist.add(p[i][1] - p[i - 1][1])

if len(dist) == 1:
    print('Yes')
    return

splited_pnt = dict()

for i in range(1, n):
    l = (p[i][1] - p[0][1]) / p[i][0]
    if l not in splited_pnt:
        splited_pnt[l] = []
    splited_pnt[l].append(i)

for l, pnt in splited_pnt.items():
    if len(p) - len(pnt) < 3:
        print('Yes')
        return

    other = [i for i in range(n) if i not in set(pnt + [0])]

    if all((p[i][1] - p[other[0]][1]) / (p[i][0] - p[other[0]][0]) == l for i in other[1:]):
        print('Yes')
        return

print('No')
