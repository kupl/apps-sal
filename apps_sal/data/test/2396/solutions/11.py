_ = int(input())
x = []
for __ in range(_) :
    s = input()
    a = s.split('/')
    c = int(a[1])
    a = a[0]
    a = a.split(')')
    a = a[0]
    a = a.split('+')
    b = int(a[1])
    a = a[0]
    a = a.split('(')
    a = int(a[1])
    x.append((a+b)/c)
d = {}
for i in x:
    d[i] = 0
for i in x :
    d[i]+=1
for i in x :
    print(d[i],end=" ")
