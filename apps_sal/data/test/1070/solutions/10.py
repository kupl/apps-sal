n=input().split( )
n[0]=int(n[0])
a=input().split( )
for i in range(n[0]):
    a[i]=int(a[i])
j=[]
c=1
if n[0]==1:
    print(1)
else:
    for i in range(n[0]-1):
        if i+1==n[0]-1 and a[i]!=a[i+1]:
            c+=1
            j.append(c)
        elif a[i]!=a[i+1]:
            c+=1
        else:
            j.append(c)
            c=1
    t=max(j)
    print(t)

