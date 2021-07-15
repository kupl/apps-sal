n,q=list(map(int,input().split()))
a=list(map(int, input().split()))
b=0
s=''
for i in range(q):
    l=list(map(int, input().split()))
    if l[0]==3:
        s+=str(a[l[1]-1]+b)+'\n'
    elif l[0]==2:
        b+=l[1]
    elif l[0]==1:
        a[l[1]-1]= l[2]-b
print(s)

