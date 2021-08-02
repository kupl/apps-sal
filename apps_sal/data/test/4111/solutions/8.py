n = int(input())
a = list(map(int, input().split()))


c = [0]
nc = [0]

fnc = sum(a[::2])
fc = sum(a[1::2])

chet = False

for s in a:

    if chet:
        c.append(c[-1] + s)
        nc.append(nc[-1])
    else:
        nc.append(nc[-1] + s)
        c.append(c[-1])

    chet = not chet

good = 0
for i in range(1, n + 1):
    sum_chet = c[i - 1] + fnc - nc[i]
    sum_nc = nc[i - 1] + fc - c[i]
    if sum_chet == sum_nc:
        good += 1


print(good)
