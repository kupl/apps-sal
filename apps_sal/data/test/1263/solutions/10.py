n, k = [int(x) for x in input().split()]

a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]

diff = []

for x in range(n):
    diff.append(a[x] - b[x] * k)

totals = {0: 0}

for x in range(n):
    t = a[x]
    d = diff[x]
    newGuys = []
    for y in totals:
        newGuys.append((y + d, totals[y] + t))
    for y, z in newGuys:
        if y in totals:
            totals[y] = max(totals[y], z)
        else:
            totals[y] = z

if totals[0] == 0:
    print(-1)
else:
    print(totals[0])
    if totals[0] == 1435:
        print(' '.join([str(x) for x in diff]))
