t=int(input())
g=list(map(int,input().split()))
k=max(g)
flag=True
i=0
while g[i]!=k:
    if i!=0 and g[i]<g[i-1]:
        print("NO")
        return
    i+=1
i+=1
while i<t and g[i]!=k:
    if i!=0 and g[i]>g[i-1]:
        print("NO")
        return
    i+=1
print("YES")
