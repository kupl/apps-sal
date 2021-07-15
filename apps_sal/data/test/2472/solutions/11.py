N=int(input())
l=[]
for _ in range(N):
    ab=list(map(int,input().split()))
    l.append(ab)
l.sort(key=lambda x:x[1])
time=0
flag=True
for i in range(N):
    time+=l[i][0]
    if time>l[i][1]:
        flag=False
        break
if flag==True:
    print('Yes')
else:
    print('No')
