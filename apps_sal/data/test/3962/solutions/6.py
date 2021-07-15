ans=0
n=int(input())
a=[]
b=[]
for i in range(n):
    x,y=list(map(int,input().split()))
    a.append(x)
    b.append(y)
a.sort()
b.sort()
#print(a)
for i in range(0,n):
    ans+=max(a[i],b[i])+1
print(ans)
        

