n = int(input())
t = list(map(int, input().split()))
c = {}
u = {}
a = [0 for _ in range(n)]
for i in range(n):
    a[i] = t[i] * i - t[i] * (n - 1 - i)
    if t[i] not in u:
        u[t[i]] = [i]
    else:
        u[t[i]].append(i)
l = []
for x in u:
    l.append(x)
l.sort()
p = len(l)
res = 0
for i in range(p - 1):
    if l[i] + 1 in u:
        l1 = len(u[l[i]])
        l2 = len(u[l[i] + 1])
        j1 = 0
        j2 = 0
        t1 = 0
        t2 = 0
        for j in range(l1 + l2):
            if j1 == l1:
                t2 += 1
                j2 += 1
                res -= t1
            elif j2 == l2:
                t1 += 1
                j1 += 1
                res += t2
            elif u[l[i]][j1] < u[l[i] + 1][j2]:
                t1 += 1
                j1 += 1
                res += t2
            else:
                t2 += 1
                j2 += 1
                res -= t1
for i in range(n):
    res += a[i]
print(res)
