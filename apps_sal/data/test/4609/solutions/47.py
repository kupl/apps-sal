n=int(input())
a=[]
for i in range(n):
    a.append(int(input()))
a=sorted(a)
ans=0
cnt=1
for i in range(n-1):

    if a[i]==a[i+1]:
        cnt+=1
    else:
        if cnt%2==1:ans+=1
        cnt=1
if cnt%2==1:ans+=1
print(ans)

