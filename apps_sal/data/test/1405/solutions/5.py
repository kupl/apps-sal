
n = int(input())
a = [int(x) for x in input().split()]
n0 = len([x for x in a if x == 0])
a = [x for x in a if x != 0]
if n0 > 0:
    a.append(0)
n = len(a)
#print("a: ", a)

pos = {}
for i in range(n):
    if a[i] in pos:
        pos[a[i]] += 1
    else:
        pos[a[i]] = 1

res = []
max_r = n0

if max_r < 2:
    max_r = 2
pr = {}
for i in range(0, n):
    for j in range(0, n):
        if i == j:
            continue
        """ 
        if (a[j], a[i]+a[j]) in pr:
            res = pr[(a[j], a[i]+a[j])] + 1
            pr[(a[i], a[j])] = res
            if res > max_r:
                max_r = res
            continue
        """
        if (a[i], a[j]) in pr:
            continue
        if a[i]+a[j] not in pos:
            continue
        res = 2
        a1 = a[i]
        a2 = a[j]
        s = a1 + a2
        m = []
        pos[a1] -= 1
        pos[a2] -= 1
        m.append(a1)
        m.append(a2)
        while (s in pos) and (pos[s] > 0):
            pos[s] -= 1
            m.append(s)
            res += 1
            a1 = a2
            a2 = s
            s = a1 + a2

        for k in range(len(m)):
            pos[m[k]] += 1
            if k > 0:
                pr[(m[k-1], m[k])] = res - k + 1
        if res > max_r:
            max_r = res
        pr[(a[i], a[j])] = res

print(max_r)

