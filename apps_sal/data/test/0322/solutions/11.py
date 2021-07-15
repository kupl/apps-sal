q=int(input())
a,s=0,0
for i in range(0,q):
    z,x=list(map(int,input().split()))
    if z>0:
        a+=1
    else:
        s+=1
if (a<=1)|(s<=1):
    print('Yes')
else:
    print('No')

