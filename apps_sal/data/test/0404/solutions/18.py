import math
b=int(input())
ans=0
for i in range(1,int(math.sqrt(b))+1):
    if b%i==0:
        ans+=1
        c=b//i
        if i!=c:
            ans+=1
print(ans)

