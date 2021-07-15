l=[1]
for i in range(32):
    l.append(l[-1]+(3*(2**i)))
m=[]
for i in range(33):
    m.append(l[i]+1)

n=[]
for i in range(33):
    n.append(m[i]*2)
    
o=[]
for i in range(33):
    o.append(m[i]+1)


t=int(input())
inp=[int(i) for i in input().split()]
for j in range(t):
    y=inp[j]
    for i in range(y):
        print(l[i],end=" ")
    print()
    for i in range(y):
        print(m[i],end=" ")
    print()
    for i in range(y):
        print(n[i],end=" ")
    print()
    for i in range(y):
        print(o[i],end=" ")
    print()
    # cook your dish here

