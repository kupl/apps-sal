a = int(input())
d = {}
dinv = {}
for i in range(a):
    b1 = input().split()
    b = list(b1)
    d[int(b[0])] = int(b[1])
    dinv[int(b[1])] = int(b[0])
c1 = []
n = 0
for i in range(a):
    n = d.get(n)
    if n in d and n != 0:
        c1 += [n]
    else:
        c1 += [n]
        break
c2 = []
for i in d.keys():
    if i not in dinv:
        k = i
        c2 += [k]
for i in range(a):
    k = d.get(k)
    if k in d and k != 0:
        c2 += [k]
    else:
        c2 += [k]
        break
c1 += [0]
c2 += [0]
for i in range(a):
    if c2[i] != 0:
        print(c2[i], end=' ')
    if c1[i] != 0:
        print(c1[i], end=' ')
    else:
        break
