n = int(input())
mps = list(map(int, input().split()))
col = list(map(int, input().split()))
st = 2
par = dict()
for i in range(n - 1):
    par[st] = par.get(st, [])
    par[st].append(mps[i])
    par[mps[i]] = par.get(mps[i], [])
    par[mps[i]].append(st)
    st += 1

queue = [1]
vis = [0] * (n + 1)
ans = 1
while len(queue):
    s = queue.pop(0)
    vis[s] = 1
    for i in par[s]:
        if not vis[i]:
            queue.append(i)
            vis[i] = 1
            if col[i - 1] != col[s - 1]:
                ans += 1

print(ans)
