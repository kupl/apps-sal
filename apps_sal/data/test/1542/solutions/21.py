n=int(input())
ls=sorted(map(int,input().split()))
q=int(input())
l=[0]*(ls[-1]+1)
for x in ls:
    l[x]+=1
for i in range(1,ls[-1]+1):
    l[i]+=l[i-1]
ans=[]
for _ in range(q):
    x=int(input())
    if x<=ls[-1]:
        ans+=[str(l[x])]
    else:
        ans+=[str(l[-1])]
print('\n'.join(ans))
