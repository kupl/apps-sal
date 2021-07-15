n = int(input())
p = []
d = dict()
for i in range(n):
    p.append(list(map(int, input().strip().split())))
    
for i in range(n):
    for j in range(i+1,n):
        x = (p[i][0] + p[j][0]) /2.
        y = (p[i][1] + p[j][1]) /2.
        if (x, y) in d.keys():
            d[(x,y)] += 1
        else:
            d[(x,y)] = 1
c = 0
for k in d.keys():
    e = d[k]
    c += e * (e-1) // 2
print(c)
