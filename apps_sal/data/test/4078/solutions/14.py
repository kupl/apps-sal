n,m=map(int,input().split())
a=list(map(int,input().split()))
ans=[]
pair=[]
for i in range(m):
    x=list(map(int,input().split()))
    #print(x)
    pair.append(x)
for i in range(n):
    for j in range(n):
        d=[]
        b=0
        for k in range(m):
            if j+1>=pair[k][0] and j+1<=pair[k][1] and (i+1<pair[k][0] or i+1>pair[k][1]) :
                b+=1
                d.append(k+1)
        d=[a[i]-a[j]+b]+d
        ans.append(d) 
        #print(*d)      
ans.sort()
print(ans[-1][0])
sz=len(ans[-1])-1
print(sz)
print(*ans[-1][1:])
