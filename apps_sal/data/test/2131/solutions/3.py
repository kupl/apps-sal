n = int(input())
orders = [0 for i in range(n)]
for i in range(n - 1):
    a, b = [int(j) - 1 for j in input().split()]
    orders[a] += 1
    orders[b] += 1

roots = []
leafs = []

for i, x in enumerate(orders):
    if x > 2:
        roots.append(i)
    elif x == 2:
        pass
    elif x == 1:
        leafs.append(i)
    else:
        raise Exception('woww')


if len(roots) > 1:
    print('No')
elif len(roots) == 0:
    print('Yes')
    print('1')
    print(' '.join([str(l + 1) for l in leafs]))
elif len(roots) == 1:
    print('Yes')
    print(str(len(leafs)))
    root = str(roots[0] + 1)
    for l in leafs:
        print(root, str(l + 1))
else:
    raise Exception('woww')
