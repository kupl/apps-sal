f = input().split()
a = int(f[0])
b = int(f[1])
am = int(f[2])
bm = int(f[3])
l = []
for i in range(bm + 1, a + 1):
    if i > bm and i >= am:
        for j in range(bm, i):
            if j <= b:
                p = []
                p.append(i)
                p.append(j)
                l.append(p)
if len(l) == 0:
    print(0)
else:
    print(len(l))
    for i in range(len(l)):
        print(l[i][0], l[i][1])
