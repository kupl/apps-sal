n=input()
k=[]
i=0
a=len(n)
x=0
p=1
q=0
while i<a:
    if n[i]=='a':
        q+=1
        x+=1
    if n[i]=='b':
        p=0
        k+=[x]
        x=0
    i+=1
k+=[x]
if p==1:
    print (q)
else:
    z=1
    for i in k:
       z*=(i+1)
    z-=1
    print (z%(10**9+7))
