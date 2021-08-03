import sys

n = int(input())

a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]

p1, p2, p3, p4 = [], [], [], []

cur = 0
for i in range(n):
    if a[i] == b[i]:
        for p in (p1, p2, p3, p4):
            p.append(a[i])
    elif cur == 0:
        p1.append(a[i])
        p2.append(a[i])
        p3.append(b[i])
        p4.append(b[i])
        cur += 1
    else:
        p1.append(a[i])
        p2.append(b[i])
        p3.append(a[i])
        p4.append(b[i])

for p in (p1, p2, p3, p4):
    if len(set(p)) == n:
        print(' '.join(str(x) for x in p))
        return

for p in (p1, p2, p3, p4):
    if len(set(p)) == n - 1:
        distinct = 0
        dpos = 0
        for i, (x, y) in enumerate(zip(p, a)):
            if x != y:
                distinct += 1
                dpos = i
        if distinct == 1:
            unused = 1
            while unused in p:
                unused += 1
            pp = list(p)
            pp[dpos] = unused
            print(' '.join(str(x) for x in pp))
            return

assert False
