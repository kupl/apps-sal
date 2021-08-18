n, m = [int(j) for j in input().split()]
adj = [set() for i in range(n)]
for i in range(m):
    l, r = [int(j) - 1 for j in input().split()]
    adj[l].add(r)
    adj[r].add(l)
if n < 7:
    print(m)
else:
    deg = 1e12
    for i in range(n):
        for j in range(i + 1, n):
            l = adj[i].intersection(adj[j])
            tmp = len(l)
            if tmp < deg:
                deg = tmp
    print(m - deg)
