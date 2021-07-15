import sys
def input():
    return sys.stdin.readline()[:-1]
H,W,N=map(int,input().split())
d=[]
for i in range(N):
    a,b=map(int,input().split())
    for j in range(-1,2):
        if not 1<a+j<H:
            continue
        for k in range(-1,2):
            if not 1<b+k<W:
                continue
            t=(a+j,b+k)
            d.append(t)
d.sort()
l=[0]*10
t=0
c=0
for i in d:
    if i==t:
        c+=1
    else:
        l[c]+=1
        t=i
        c=1
l[c]+=1
l[0]=(H-2)*(W-2)-sum(l)+1
print(*l,sep="\n")
