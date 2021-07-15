n , q = list(map(int,input().split()))
tasks=[]
servers = [0]*n
for _ in range(q):
    tasks.append(tuple(map(int,input().split())))

for t,k,d in tasks:
    a = []
    for i in range(n):
        if t>=servers[i]:
            a.append(i)
    if len(a)>=k:
        total = 0
        for s in range(k):
            total+=a[s]+1
            servers[a[s]]=t+d
        print(total)
    else:
        print(-1)

