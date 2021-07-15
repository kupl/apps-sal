import sys
n,m=list(map(int,sys.stdin.readline().split()))

Tasks=list(map(int,sys.stdin.readline().split()))

p=1
ans=0
for item in Tasks:
    x=item-p
    if(x<0):
        x=n+x
    ans+=x
    p=item
print(ans)



