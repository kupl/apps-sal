N = int(input())
AB = [tuple(map(int,input().split())) for i in range(N-1)]
M = int(input())
UV = [tuple(map(int,input().split())) for i in range(M)]

es = [[] for i in range(N)]
for i,(a,b) in enumerate(AB):
    a,b = a-1,b-1
    es[a].append((b,i))
    es[b].append((a,i))

paths = [0] * M
for i,(u,v) in enumerate(UV):
    u,v = u-1,v-1
    stack = [u]
    visited = [0] * N
    visited[u] = 1
    edges = [-1] * N
    while stack:
        s = stack.pop()
        for to,j in es[s]:
            if visited[to]: continue
            visited[to] = 1
            edges[to] = j
            stack.append(to)
            if to == v:
                break
        else:
            continue
        while edges[v] >= 0:
            j = edges[v]
            paths[i] |= (1<<j)
            a,b = AB[j]
            a,b = a-1,b-1
            v = a if a!=v else b
        break

dp = [0] * (1<<M)
for b in range(1,1<<M):
    k = len(bin(b))-3
    dp[b] = dp[b-2**k] | paths[k]

ans = 0
for i,d in enumerate(dp):
    b = N-1 - bin(d).count('1')
    ans += 2**b if bin(i).count('1')%2==0 else -2**b
print(ans)
