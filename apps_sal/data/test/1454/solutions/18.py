a=[int(a)for a in input().split()]
b=list(list())
su=0
ans=0
cp=0
for j in range (a[0]):
        c=[int(a) for a in input().split()][:a[1]]
        b.append(c)
for i in range(a[0]-1,-1,-1):
    for j in range(a[1]-1,-1,-1):
        if b[i][j]==0:
            b[i][j]=int(min(b[i][j+1],b[i+1][j]))-1
for z in b:
    for r in z:    
        su+=r
for i in range(a[0]):
    for j in range(a[1]):
        try:
            if b[i][j]>=b[i+1][j]:
                ans=-1
                break
        except:
            cp+=1
            #print(i,j)
        try:
            if b[i][j]>=b[i][j+1]:
                ans=-1
                break
        except:
            cp+=1
            #print(i,j)

if ans==-1:
    print(-1)
else:
    print(su)
