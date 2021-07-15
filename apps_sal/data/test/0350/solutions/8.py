n=int(input())
L=[int(x) for x in input().split()]
L.sort()
L=L[::-1]
ans=0
dis=L[0]+1
for i in L:
    ans+=max(0,min(dis,i))
    dis=min(dis,i)-1
print(ans)

