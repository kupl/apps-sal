n=int(input())
a=list(map(int,input().split()))

cnt=0
m=1

for i in range(n):
    if a[i]==m:
        cnt+=1
        m+=1
        
if cnt==0:
    print((-1))
else :
    print((n-cnt))

