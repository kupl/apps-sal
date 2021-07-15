a,b,k=list(map(int,input().split()))

ans=[]

for i in range(k):
    if a+i<=b-i:
        ans.append(a+i)
        ans.append(b-i)

ans=set(ans)
ans=list(ans)
ans.sort()


for a in ans:
    print(a)


