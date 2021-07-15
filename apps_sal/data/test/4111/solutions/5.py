n=int(input())
L=[int(i) for i in input().split()]
e=0
d=0
for i in range(n):
    if (i+1)%2==0:
        e+=L[i]
    else:
        d+=L[i]
s=0
e1=0
d1=0
#print(e, d)
for i in range(n-1, -1, -1):
    if (i+1)%2==0:
        e=e-L[i]
        if e+e1==d+d1:
            s+=1
        d1+=L[i]
    else:
        d=d-L[i]
        if e+e1==d+d1:
            s+=1
        e1+=L[i]
    #print(e, d, e1, d1)
print(s)

