n = int(input())
a = list(map(int, input().split()))
vis = [False for i in range(n + 1)]
c = {}
for i in range(n):
    if a[i] is not 0:
        vis[a[i]] = True
    else:
        c[i] = True
d = {}
for i in range(1, n + 1):
    if vis[i] == False:
        d[i] = True
delete = []
for i in c:
    if i + 1 in d:
        k = 0
        for j in d:
            if j is not i + 1:
                a[i] = j
                k = j
                break
        d.pop(k)
        delete.append(i)
for i in delete:
    c.pop(i)
p = [i for i in c]
q = [i for i in d]
for i in range(len(p)):
    a[p[i]] = q[i]
print(' '.join(map(str, a)))
