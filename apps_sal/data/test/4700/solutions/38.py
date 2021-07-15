n,m = list(map(int,input().split()))
h = [0]+list(map(int,input().split()))

route = [[0] for _ in range(n+1)]
for _ in range(m):
    a,b = list(map(int,input().split()))
    route[a].append(h[b])
    route[b].append(h[a])

cnt=0
for i in range(1,n+1):
    if h[i]>max(route[i]):
        cnt+=1
print(cnt)

