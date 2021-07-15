

num = int(input())
l = list()
for i in range(num):
    f = list(map(int, input().split()))
    a = f[0]
    b = f[1]
    tup = (a, b)
    l.append(tup)
    
l.sort()
c = 0
for el in l:
    a = el[0]
    b = el[1]
    if b >= c:
        c = b
    else:
        c = a 

print(c)
