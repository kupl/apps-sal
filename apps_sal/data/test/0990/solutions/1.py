n = int(input())
adj = [[] for _ in range(n)]
adj_dict = dict()

for i in range(n - 1):
    a, b = [int(x) - 1 for x in input().split()]
    adj[a].append(b)
    adj[b].append(a)
    if a > b:
        adj_dict[(b, a)] = i
    else:
        adj_dict[(a, b)] = i

m = int(input())
uv = []
for _ in range(m):
    uv.append([int(x) - 1 for x in input().split()])


def dfs(p, v, dest):
    if v == dest:
        return [v]
    if p != -1 and len(adj[v]) == 1:
        return False
    for nv in adj[v]:
        if nv == p:
            continue
        ret = dfs(v, nv, dest)
        if ret:
            return ret + [v]
    return False


edgest = [0] * (2 ** m)
for i, (u, v) in enumerate(uv):
    ret = dfs(-1, u, v)
    for uu, vv in zip(ret, ret[1:]):
        if uu > vv:
            uu, vv = vv, uu
        if (uu, vv) in adj_dict:
            edgest[1 << i] |= (1 << adj_dict[(uu, vv)])

for i in range(1, 2 ** m):
    lsb = i & (-i)
    edgest[i] = edgest[i ^ lsb] | edgest[lsb]

dp = [0] * (2 ** m)
dp[0] = 1 << (n - 1)
ans = dp[0]
for i in range(1, 2 ** m):
    lsb = i & (-i)
    lim = bin(edgest[i] ^ edgest[i ^ lsb]).count('1')
    dp[i] = dp[i ^ lsb] >> lim
    if bin(i).count('1') % 2 == 0:
        ans += dp[i]
    else:
        ans -= dp[i]
print(ans)
