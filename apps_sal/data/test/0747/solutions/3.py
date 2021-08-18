import sys
f = sys.stdin
n, x = map(int, f.readline().strip().split())

kon = []
kon0 = []
kon1 = []
for i in range(n):
    ti, hi, mi = map(int, f.readline().strip().split())
    kon.append([ti, hi, mi])
    if ti == 0:
        kon0.append([hi, mi])
    else:
        kon1.append([hi, mi])


def ksort(item):
    if item[0] <= x:
        return -item[1]
    else:
        return item[0] - item[1] / 10000


kon0.sort(key=ksort)
kon1.sort(key=ksort)


t0 = kon0[:]
t1 = kon1[:]
tx = x

s = 0
i0 = 0
not_end = True
while not_end:
    if i0 % 2 == 0 and len(kon0) > 0 and x >= kon0[0][0]:
        s += 1
        x += kon0[0][1]
        del kon0[0]
        kon0.sort(key=ksort)
        kon1.sort(key=ksort)
        i0 += 1
    elif i0 % 2 == 1 and len(kon1) > 0 and x >= kon1[0][0]:
        s += 1
        x += kon1[0][1]
        del kon1[0]
        kon0.sort(key=ksort)
        kon1.sort(key=ksort)
        i0 += 1
    else:
        not_end = False


s1 = s

kon0 = t0
kon1 = t1
x = tx

s = 0
i0 = 1
not_end = True
while not_end:
    if i0 % 2 == 0 and len(kon0) > 0 and x >= kon0[0][0]:
        s += 1
        x += kon0[0][1]
        del kon0[0]
        kon0.sort(key=ksort)
        i0 += 1
    elif i0 % 2 == 1 and len(kon1) > 0 and x >= kon1[0][0]:
        s += 1
        x += kon1[0][1]
        del kon1[0]
        kon1.sort(key=ksort)
        i0 += 1
    else:
        not_end = False


print(max(s, s1))
