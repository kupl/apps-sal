n=int(input())
p=[7]
r=[]
cnt=0
for i in range(0,8):
    p.append(0)
a=list(map(int,input().split()))
for i in a:
    p[i]=p[i]+1
if(p[5]>0 or p[7]>0):
    print("-1")
    return
if(p[1]+p[2]<n/3):
    print("-1")
    return
while(p[1]>0 and p[3]>0 and p[6]>0):
    if(p[3]>0 and p[6]>0):
        r.append("1 3 6")
        p[1]=p[1]-1
        p[3]=p[3]-1
        p[6]=p[6]-1
        cnt=cnt+1
while(p[1]>0 and p[2]>0 and p[4]>0):
    if(p[2]>0 and p[4]>0):
        r.append("1 2 4")
        p[1]=p[1]-1
        p[4]=p[4]-1
        p[2]=p[2]-1
        cnt=cnt+1
while(p[1]>0 and p[2]>0 and p[6]>0):
    if(p[2]>0 and p[6]>0):
        r.append("1 2 6")
        p[1]=p[1]-1
        p[2]=p[2]-1
        p[6]=p[6]-1
        cnt=cnt+1
if(cnt!=n/3):
    print("-1")
    return
else:
    for i in r:
        print(i)
return

