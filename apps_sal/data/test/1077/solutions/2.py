a = [int(i) for i in (str(input())).split()]
n = a[0]
m = a[1]
a = [int(i) for i in (str(input())).split()]
maxmin = n // m

groups = {}
for i in a:
    groups[i] = 0
for i in range(m):
    groups[i + 1] = 0

for i in a:
    groups[i] += 1
changes = 0
for i in range(1, m + 1):
    while groups[i] < maxmin:
        change = False
        for n, j in enumerate(a):
            # print(j)
            if j <= m:
                continue
            groups[j] -= 1
            a[n] = i
            groups[i] += 1
            # print('kek')
            changes += 1
            change = True
            if groups[i] >= maxmin:
                break

        if groups[i] >= maxmin:
            continue

        for n, j in enumerate(a):
            # print(j)
            if groups[j] <= maxmin:
                continue
            # print(groups[j])
            groups[j] -= 1
            a[n] = i
            groups[i] += 1
            changes += 1
            change = True
            if groups[i] >= maxmin:
                break

print('%s %s' % (maxmin, changes))
for i in a:

    print(i, end=' ')
