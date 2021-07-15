n=int(input())
a=input()
ans=''
now=0
dop=1
while now<=n:
    ans+=a[now]
    dop+=1
    now+=dop
print(ans)
    

