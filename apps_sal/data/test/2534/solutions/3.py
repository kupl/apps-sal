r, c = map(int, input().split())
k = []
for _ in range(r):
    a = []
    a = list(map(int, input().split()))
    k.append(a)
rmin = []
cmax = []
for i in range(r):
    rmin.append(min(k[i]))
for j in range(c):
    b = k[0][j]
    for i in range(r):
        if b < k[i][j]:
            b = k[i][j]
    cmax.append(b)
if(set(rmin).intersection(set(cmax))):
    print(*set(rmin).intersection(set(cmax)))
else:
    print('GUESS')
