a = int(input())
l = []
lf = []
rt = []
for i in range(a):
    s = input().split()
    l.append(s)
    lf.append(int(l[i][0]))
    rt.append(int(l[i][1]))
p = lf.count(1)
q = rt.count(0)
r = rt.count(1)
s = lf.count(0)
k = []
k.append(p + q)
k.append(r + s)
k.append(p + r)
k.append(q + s)
print(min(k))
