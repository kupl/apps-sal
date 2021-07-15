n,m,k=map(int,input().split())
l=set(map(int,input().split()))
i=1
for _ in range(k):
    u,v=map(int,input().split())
    if i in l: break
    if i==u: i=v
    elif i==v: i=u
print(i)
