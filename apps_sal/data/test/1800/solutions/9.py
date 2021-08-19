s = input()
num = [int(x) for x in s.split()]
n, m = num[0], num[1]
s = input()
a = [int(x) for x in s.split()]
t1 = [0 for x in range(m)]
r1 = [0 for x in range(m)]
for i in range(m):
    s = input()
    num = [int(x) for x in s.split()]
    t1[i], r1[i] = num[0], num[1]
    r1[i] = r1[i] - 1
    if t1[i] is 2:
        t1[i] = -1

t = []
r = []
for i in range(m):
    while len(r) != 0 and r[-1] <= r1[i]:
        t.pop()
        r.pop()
    t.append(t1[i])
    r.append(r1[i])

# print(t)
# print(r)

m = len(t)
b = [0 for x in range(n)]
last = 0
for i in range(m - 1, -1, -1):
    if r[i] > last:
        last = r[i]
        b[r[i]] = t[i]

# print(b)
r = []
r.extend(a)
for i in range(n - 1, -1, -1):
    if b[i] is 1:
        c = sorted(a[:i + 1])
        c.extend(a[i + 1:])
        typ = b[i]
        r = []
        r.extend(c)

        le = 0
        ri = i - 1
        tp = typ
        for j in range(i - 1, -1, -1):
            if b[j] is not 0:
                tp = b[j]
            if tp == typ:
                r[j] = c[ri]
                ri = ri - 1
            else:
                r[j] = c[le]
                le = le + 1
        break
    elif b[i] is -1:
        c = sorted(a[:i + 1])
        c.reverse()
        c.extend(a[i + 1:])
        typ = b[i]
        r = []
        r.extend(c)

        le = 0
        ri = i - 1
        tp = typ
        # print(c)
        for j in range(i - 1, -1, -1):
            if b[j] is not 0:
                tp = b[j]
            if tp == typ:
                r[j] = c[ri]
                ri = ri - 1
            else:
             #       print(le)
             #       print(c[le])
                r[j] = c[le]
                le = le + 1

          #  print(r)
        break

# print(c)
for j in range(len(r)):
    print(r[j], end=' ')
print()
