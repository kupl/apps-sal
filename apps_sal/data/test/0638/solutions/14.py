(n, m) = map(int, input().split())
t = list(map(int, input().split()))
t2 = []
cur = 0
res = []
for i in t:
    if sum(t2) + i <= m:
        t2.append(i)
        res.append(0)
    else:
        j = 0
        t3 = t2[:]
        while sum(t3) + i > m:
            t3.remove(max(t3))
            j += 1
        t2.append(i)
        res.append(j)
for i in res:
    print(i, end=' ')
