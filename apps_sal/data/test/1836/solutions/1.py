n, m = list(map(int, input().split()))

edges = []
max_lens = []
for i in range(n+1):
    edges.append(set())
    max_lens.append(1)
    
for i in range(m):
    u, v = list(map(int, input().split()))
    edges[u].add(v)
    edges[v].add(u)


maximum = 0
for i in range(1, n+1):

    for j in edges[i]:
        if j < i:
            max_lens[i] = max(max_lens[i], max_lens[j] + 1)


    maximum = max(len(edges[i]) * max_lens[i], maximum)

print(maximum)
        
        
    
    

    




