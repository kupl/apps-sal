n=int(input())
l=[input().split() for i in range(n)]
l2=[x for x in range(n)]
base=list(zip(l2,l))
ans=sorted(base, key=lambda x: int(x[1][1]),reverse=True)
ans=sorted(ans,key=lambda x: x[1][0])

for i in range(n):
    print(1+ans[i][0])
