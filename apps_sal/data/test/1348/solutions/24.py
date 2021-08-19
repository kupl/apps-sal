def solve(n, k, d):
    dist = [[] for i in range(n)]
    for u in range(n):
        dist[d[u]].append(u)
    if len(dist[0]) != 1:
        return []
    ans = []
    for t in range(1, n):
        nxt = []
        j = 0
        lim = k if t == 1 else k - 1
        ctr = 0
        for u in dist[t]:
            if ctr == lim:
                ctr = 0
                j += 1
            if j == len(dist[t - 1]):
                return []
            else:
                ans.append((dist[t - 1][j] + 1, u + 1))
                ctr += 1
    return ans


(n, k) = list(map(int, input().split()))
d = [int(x) for x in input().split()]
ans = solve(n, k, d)
if ans == []:
    print(-1)
else:
    print(len(ans))
    for e in ans:
        print(*e)
