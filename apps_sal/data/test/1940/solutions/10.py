n,k=map(int,input().split())
ip=list(map(int,input().split()))
count=0
for i in ip:
    if i%k==0:
        count+=i//k
    else:
        count+=(i//k)+1
if count %2==0:
    print(count//2)
else:
    print(count//2 + 1)
