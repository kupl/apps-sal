from functools import reduce


def add(a, b):
    return a + b


n, m = [int(x) for x in input().split()]
neigh = [[] for x in range(n)]
for i in range(m):
    x, y = [int(a) for a in input().split()]
    neigh[x - 1].append(y)
    neigh[y - 1].append(x)
oneneigh, twoneigh, nneigh = 0, 0, 0
for i in neigh:
    if len(i) == 1:
        oneneigh += 1
    elif len(i) == 2:
        twoneigh += 1
    else:
        nneigh += 1
if twoneigh == n:
    print('ring topology')
elif oneneigh == 2 and twoneigh == n - 2:
    print('bus topology')
elif nneigh == 1 and oneneigh == m:
    print('star topology')
else:
    print('unknown topology')
