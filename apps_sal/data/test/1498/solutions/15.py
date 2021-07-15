n, q = list(map(int, input().split()))
servers = [i for i in range(1, n+1)]
res, used = [], {}
for i in range(q):
    t, s, d = list(map(int, input().split())) 
    finish = t + d
    for i in list(used.keys()):
        if t >= i:
            servers += used[i]
            servers.sort()
            del used[i]
    if s > len(servers):
        res.append(-1)
        continue
    if not used.get(finish):
        used[finish] = servers[:s]
    else:
        used[finish] += servers[:s]
    res.append(sum(servers[:s]))
    servers = servers[s:]
for i in res: 
    print(i)

