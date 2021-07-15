import math
n=int(input())
ans=1
dic={}
for i in range(2,n+1):
    tmp=i
    for j in range(2,i+1):
        while tmp%j==0:
            tmp//=j
            if j in dic:
                dic[j]+=1
            else:
                dic[j]=1
for v in dic.values():
    ans=(ans*(v+1))%(10**9+7)
print(ans)
