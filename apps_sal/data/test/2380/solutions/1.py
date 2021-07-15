n,m=list(map(int,input().split()))
a=list(map(int,input().split()))
a.sort()
num=[]
for i in range(m):
    num.append(list(map(int,input().split())))
num.sort(reverse=True,key=lambda x: x[1])
cnt=0
for i in range(n):
    if cnt==m:
        break
    if num[cnt][0]==0:
        cnt+=1
    if cnt==m:
        break
    if a[i]>=num[cnt][1]:
        break
    a[i]=num[cnt][1]
    num[cnt][0]-=1
print((sum(a)))

