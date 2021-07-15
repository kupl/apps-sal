import sys
input=sys.stdin.readline
def fun(k):
    nonlocal li,t
    tem=[]
    count=0
    for i in li:
        if(i[0]>=k):
            tem.append(i)
            count+=1
    if(count>=k):
        ans=0
        for i in range(k):
            ans+=tem[i][1]
        if(ans<=t):
            return True
        else:
            return False
    else:
        return False
                  
n,t=map(int,input().split())
li=[]
for _ in range(n):
    li.append(list(map(int,input().split()))+[_])
li.sort(key=lambda x:x[1])
l=0
r=n
while(r-l>1):
    mid=(l+r)//2
    if(fun(mid)):
        l=mid
    else:
        r=mid
fin=0
for i in range(l,r+1):
    if(fun(i)):
        fin=i
print(fin)
print(fin)
tem=[]
for i in range(n):
    if(li[i][0]>=fin):
        tem.append(li[i][2]+1)
print(*tem[:fin])
