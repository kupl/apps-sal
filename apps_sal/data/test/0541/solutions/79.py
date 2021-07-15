n,m=map(int,input().split())
ans=0
head=1
from operator import itemgetter as it
for x,y in sorted([list(map(int,input().split()))for i in range(m)],reverse=0,key=lambda x:(it(1)(x)*(n+1)*10-it(0)(x))):
    if not(x<head <=y):
        head=y
        ans+=1
print(ans)
