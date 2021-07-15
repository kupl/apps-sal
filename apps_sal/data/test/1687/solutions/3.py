n=int(input())
lis=input().split()
for i in range(len(lis)):
    lis[i]=int(lis[i])
m=min(lis)
check=1
for i in range(len(lis)):
    if lis[i]%m!=0:
        check=0
if check==0:
    print(-1)
else:
    print(m)

