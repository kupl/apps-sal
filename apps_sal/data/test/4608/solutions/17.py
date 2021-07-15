n=int(input())
a=[]
for _ in range(n):
    a.append(int(input()))
now=0
cnt=0
visit=[0 for _ in range(n)]
Flag=False
while now != 1:
    if visit[now] != 0:
        Flag=True
        break
    else:
        visit[now]=1
        now=a[now]-1
        cnt+=1
if Flag:
    print('-1')
else:
    print(cnt)

