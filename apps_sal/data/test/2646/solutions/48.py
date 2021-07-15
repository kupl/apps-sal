import copy
N, M = map(int, input().split())
res = [[] for i in range(N+5)]


for i in range(M) :
    a,b = map(int, input().split())
    a -= 1
    b -= 1
    res[a].append(b)
    res[b].append(a)
    
pre = [-1] * N
dist = [-1] * N
d = 1
dl = []
pre[0] = 0
dist[0] = 0
dl.append(0)

while(len(dl) != 0) :
    a = dl[0]
    dl.pop(0)
    for i in res[a] :
        if(dist[i] != -1):
            continue
        dist[i] = dist[a] + 1
        pre[i] = a
        dl.append(i)
        
for i in range(N) :
    if(i == 0) :
        print("Yes")
        continue
    print(pre[i] + 1)
