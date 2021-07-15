a,b,c=map(int,input().split())
k=b+c
x=list(map(int,input().split()))
y=list(map(int,input().split()))
i=0
z=[]
while i<len(x):
    z=z+[max(x[i],y[i])-min(x[i],y[i])]
    i=i+1
z.sort()
i=0
while i<k:
    if z[len(z)-1]!=0:
        z[len(z)-1]=z[len(z)-1]-1
    else:
        if (k-i)%2==1:
            z=[1]
        break
    z.sort()
    i=i+1
s=0
for elem in z:
    s=s+elem**2
print (s)
