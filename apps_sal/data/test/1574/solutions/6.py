n, m = (int(x) for x in input().split())

adj = [0] * n

for i in range(n):
    adj[i] = []


for i in range(m):
    a, b = (int(x) for x in input().split())
    adj[a-1].append(b - 1)
    adj[b-1].append(a - 1)

# print(adj)

best = 1000000

for i in range(n):
    cur_set = set(adj[i])
    for j in adj[i]:
        for k in adj[j]:
            if k in cur_set:
                best = min(best, len(adj[i]) + len(adj[j]) + len(adj[k]) - 6)

if best == 1000000:
    best = - 1

print(best)

