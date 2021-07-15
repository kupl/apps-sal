n,m=list(map(int,input().split()))
a=list(map(int,input().split()))
t=list(map(int,input().split()))
x=sum(t)
for i in range(n-x+1):
    freq=[0]*m
    for j in range(i,i+x):
        freq[a[j]-1]+=1
    flag=True
    for j in range(m):
        if freq[j]!=t[j]:
            flag=False
            break 
    if flag:
        break
if flag:
    print("YES")
else:
    print("NO")


