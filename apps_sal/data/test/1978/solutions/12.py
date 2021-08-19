def gns():
    return list(map(int, input().split()))


n = int(input())
mp = []
for i in range(n):
    mp.append(input())


def bfs(i):
    nxt = [i]
    ans = [None] * n
    ans[i] = 0
    v = [False] * n
    v[i] = True
    p = 0
    while len(nxt) > 0:
        p += 1
        nxt_ = []
        for ni in nxt:
            for nn in range(n):
                if v[nn] or mp[ni][nn] == '0':
                    continue
                v[nn] = True
                ans[nn] = p
                nxt_.append(nn)
        nxt = nxt_
    return ans


dis = [None] * n
for i in range(n):
    dis[i] = bfs(i)
m = int(input())
ms = gns()
ms = [x - 1 for x in ms]
ans = [ms[0]]
l = ms[0]
for i in range(1, m - 1):
    c = ms[i]
    cn = ms[i + 1]
    if dis[l][cn] <= dis[l][c]:
        ans.append(c)
        l = c
ans.append(ms[-1])
ans = [x + 1 for x in ans]
print(len(ans))
print(' '.join(map(str, ans)))
