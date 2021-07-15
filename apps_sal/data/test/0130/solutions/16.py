n,m=list(map(int,input().split()))
ls=[]
for i in range(n):
    l=list(str(input()))
    ls.append(l)
minr=1000
maxr=-1
minc=1000
maxc=-1
c=0
for i in range(n):
    for j in range(m):
        if ls[i][j]=='B':
            c+=1
            if minr>i:
                minr=i
            if maxr<i:
                maxr=i
            if minc>j:
                minc=j
            if maxc<j:
                maxc=j
if c==0:
    print(1)
    return
elif c==1:
    print(0)
    return
else:
    a=max(maxr-minr+1,maxc-minc+1)
    if a>m or a>n:
        print(-1)
        return
    else:
        print(a*a-c)
        return

