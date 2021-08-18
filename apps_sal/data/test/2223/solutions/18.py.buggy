n = int(input())
if n % 2 == 1:
    print(-1)
    return

adj = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    u, v = list(map(int, input().split()))
    adj[u].append(v)
    adj[v].append(u)

cnt = [1] * (n + 1)
prt = [-1] * (n + 1)
prt[1] = 1
stk = [1]
while stk:
    u = stk[-1]
    k = False
    for v in adj[u]:
        if prt[v] == -1:
            prt[v] = u
            stk.append(v)
            k = True
    if not k:
        stk.pop()
        cnt[prt[u]] += cnt[u]
res = 0
for j in cnt[2:]:
    if j % 2 == 0:
        res += 1
print(res)
