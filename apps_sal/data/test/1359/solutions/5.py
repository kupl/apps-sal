n, m = list(map(int, input().split()))
adj = []
for i in range(n):
    adj.append([])
for i in range(m):
    a, b = list(map(int, input().split()))
    adj[a - 1].append(b)
ans = 0
ncr = []
for i in range(n):
    m = {}
    for j in adj[i]:
        for k in adj[j - 1]:
            if(k in list(m.keys())):
                m[k] += 1
            else:
                m[k] = 1
    for j in list(m.keys()):
        if(j != i + 1):
            ans += (m[j] * (m[j] - 1)) // 2
print(ans)
