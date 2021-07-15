n=int(input())
lis=input().split()
for i in range(n):
    lis[i]=int(lis[i])
def diff(a):
    m=a[1]-a[0]
    for i in range(1,len(a)-1):
        if a[i+1]-a[i]>m:
            m=a[i+1]-a[i]
    return m

lis2=[]
for i in range(1,n-1):
    lis2.append(diff(lis[:i]+lis[i+1:]))
print(min(lis2))
    
               

