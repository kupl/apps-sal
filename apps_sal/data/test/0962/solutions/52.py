N,M = map(int,input().split())
AB = [tuple(map(int,input().split())) for i in range(M)]
es = [[] for i in range(N)]
for a,b in AB:
    a,b = a-1,b-1
    es[a].append(b)

from collections import deque
mindist = N
opt = None
for g,tos in enumerate(es):
    for s in tos:
        q = deque([(s,0)])
        prev = [-1]*N
        dist = [N]*N
        dist[s] = 0
        while q:
            v,d = q.popleft()
            for to in es[v]:
                if to==g: break
                if d+1 >= dist[to]: continue
                dist[to] = d+1
                prev[to] = v
                q.append((to,d+1))
            else:
                continue
            break
        else:
            continue
        if d+1 >= mindist: continue
        mindist = d+1
        opt = [g,v]
        while prev[opt[-1]] >= 0:
            opt.append(prev[opt[-1]])
if opt:
    ans = [o+1 for o in opt]
    print(len(ans))
    print(*ans, sep='\n')
else:
    print(-1)
