(n, k) = [int(x) for x in input().split()]
guests = list(input())
doors = dict()
gt = dict()
opened = 0
f = True
for u in guests:
    gt[u] = gt.get(u, 0) + 1
for i in guests:
    if i not in doors:
        doors[i] = 1
        opened += 1
    else:
        doors[i] += 1
    if opened > k:
        print('YES')
        f = False
        break
    if doors[i] == gt[i]:
        opened -= 1
if f:
    print('NO')
