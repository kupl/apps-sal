n = int(input())

zi = [int(x) for x in input().split()]



g = n
res = []
while g!=1:
    res.append(g)
 
    g = zi[g-2]

res.append(1)

zz = reversed(res)

zs = [str(x) for x in zz]

s = ' '.join(zs)

print(s)



