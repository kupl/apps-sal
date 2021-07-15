n=int(input())
a=list(map(int,input().split()))
vessels=[]
ans=[]
index=[]
for i in range(n):
    vessels.append([0,a[i]])
    index.append(i+1)    
m=int(input())
for i in range(m):
    a=input()
    if a[0]=='1':
        a,p,x=list(map(int,a.split()))
        p-=1
        tt=set()
        while p<n and x>0:
            t=vessels[p][1]-vessels[p][0]
            if x>t:
                x-=t
                vessels[p][0]=vessels[p][1]
                tt.add(p)
                p=index[p]
            else:
                vessels[p][0]+=x
                break
        for i in tt:
            index[i]=p
    else:
        a,b=list(map(int,a.split()))
        ans.append(vessels[b-1][0])
print('\n'.join(map(str,ans)))
