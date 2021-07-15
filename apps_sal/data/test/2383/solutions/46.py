n=int(input())
a=list(map(int,input().split()))
cnt=0
num=1
for i in range(len(a)):
    if a[i]!=num:
        cnt+=1
    else:
        num+=1
if num==1:
    print(-1)
else:
    print(cnt)
