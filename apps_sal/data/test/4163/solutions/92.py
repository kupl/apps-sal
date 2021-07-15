a=[ ]
n=int(input())
for i in range(0,n):
    a.append(input().split())
    a[i][0]=int(a[i][0])
    a[i][1]=int(a[i][1])
cnt=0
flg=False
j=0
while j<n and flg==False:
    if(a[j][1]==a[j][0]):
        cnt=cnt+1
    else:
        cnt=0
    if(cnt==3):
        flg=True
    j=j+1
if(flg==True):
    print("Yes")
else:
    print("No")

