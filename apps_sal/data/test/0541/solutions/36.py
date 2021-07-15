n,m=map(int,input().split())
A=[]
for i in range(m):
    a,b=map(int,input().split())
    a-=1 ;b-=1
    A.append([a,b])

A=sorted(A, key=lambda x:x[1])
ans=0
last=-5000
for l in A:
    #print(a,b)
    if last<l[0]:
        ans+=1
        last=l[1]-1
print(ans)
