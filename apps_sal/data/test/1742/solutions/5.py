n, m = [int(x) for x in input().split()]
q = [int(x) for x in input().split()]
helpers = [[] for i in range(n + 5)]
helping = [0] * 300005
ans, removed = 0, 0
for i in range(m):
    u, v = [int(c) for c in input().split()]
    helpers[v].append(u)

for i in helpers[q[-1]]:
    helping[i] += 1

for i in range(n - 2, -1, -1):
    remaining = n - 1 - i - removed
    if(helping[q[i]] == remaining):
        removed += 1
        ans += 1
    else:
        for k in helpers[q[i]]:
            helping[k] += 1
        
print(ans)

    

