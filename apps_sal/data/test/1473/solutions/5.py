n = int(input())
d1 = dict()
d2 = dict()
ar = [0] * (30000000)
for i in range(n):
    a, b = map(int, input().split())
    ar[a] += 1
    ar[b] += 1    
    d1[a] = b
    d2[b] = a
if n % 2 == 0:
    x = 0
    ar1 = []
    ar2 = []
    while x in d1:
        ar1.append(d1[x])
        x = d1[x]
    x = 0
    while x in d2:
        ar2.append(d2[x])
        x = d2[x]
    ar2 = list(reversed(ar2))
    for i in range(len(ar2)):
        print(ar2[i], end = ' ')
        print(ar1[i], end = ' ')
else:
    arx = []
    for i in range(1000000):
        if ar[i] == 1:
            arx.append(i)
    a = arx[0]
    b = arx[1]
    if b in d2:# a in d2
        a, b = b, a
    x = 0
    ar1 = []
    ar2 = []
    while x in d1:
        if d1[x] != 0:
            ar1.append(d1[x])
        x = d1[x]
        if x == 0:
            break
    
    x = a
    while x in d2:
        ar2.append(d2[x])
        x = d2[x]    
    ar2 = list(reversed(ar2))
    for i in range(len(ar2)):
        print(ar2[i], end = ' ')
        print(ar1[i], end = ' ')    
    print(a)
