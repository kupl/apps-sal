l=input().split()
s=input().split()
r=[0]*3
for i in range(3):
    l[i]=int(l[i])
    s[i]=int(s[i])
    r[i]=l[i]-s[i]
k=0
m,n=0,0
for i in range(3):
    if(r[i]>=0):
        m+=r[i]//2
    else:
        k+=1
        r[i]=-r[i]
        n+=r[i]
if(k==3):
    print("No")
else:
    if(m>=n):
        print("Yes")
    else:
        print("No")
