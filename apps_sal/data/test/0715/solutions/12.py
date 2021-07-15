a = input()
b = input()
c = input()
d = input()

eles = [a, b , c , d]
elems = [a[2:], b[2:], c[2:], d[2:]]
#print(elems)
g = []
l = [len(elems[0]),len(elems[1]), len(elems[2]), len(elems[3])]
#print(l)
for i in range(4):
    ele = l[i]
    r = []
    for j in range(4):
        
        if i == j :
            continue
        else:
            ratio = ele / l[j]
            #print(ratio)
            r.append(ratio)
    #print(r)
    count = 0
    for k in range(len(r)):
        if r[k] <= 0.5  :
            count += 1
    if count == 3 :
        g.append(i)
    else:
        count1 = 0
        for c in range(len(r)):
            if r[c] >= 2:
                count1 += 1
        if count1 == 3:
            g.append(i)
            
    

if len(g) == 1:
    print(eles[g[0]][0])
else:
    print('C')

