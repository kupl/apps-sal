import math
q=int(input())
num=[0]*(10**5+5)
ans=[0]*(10**5+5)
num[2]=1
for i in range(3,10**5+2,2):
    yn=0
    for j in range(2,int(math.sqrt(i))+1):
        if i%j==0:
            yn=1
            break
    if yn==0:
        num[i]=1
        if num[(i+1)//2]==1:
            ans[i]=1
for i in range(1,len(num)):
    ans[i]=ans[i-1]+ans[i]
for i in range(q):
    l,r=list(map(int,input().split()))
    print((ans[r]-ans[l-1]))

