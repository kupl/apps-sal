n = int(input())
c  = [0] + [int(j) for j in input().split()]
a  = [0] + [int(j) for j in input().split()]
 
vis = [0] * (n+1)
ans = 0
for i in range(1,n+1):
    x = i
    while vis[x] == 0:
        vis[x] = i
        x = a[x]
    if vis[x] != i:
        continue
    v = x
    mn = c[x]
    while a[x] != v:
        x = a[x]
        mn = min(mn,c[x])
    ans+=mn
print(ans)
