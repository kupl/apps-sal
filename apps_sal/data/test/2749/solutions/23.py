
h,w=list(map(int,input().split()))
n=int(input())
a=list(map(int,input().split()))

bb=[[0]*w for i in range(h)]
idx=0
kk=0
for i in range(h):
    if i%2==0:
        wst=0
        wed=w
        wpt=1
    else:
        wst=w-1
        wed=-1
        wpt=-1
        
    for j in range(wst,wed,wpt):
        if kk>=a[idx]:
            idx+=1
            kk=0
        bb[i][j]=str(idx+1)
        kk+=1
        
for i in range(h):
    print((" ".join(bb[i])))    

