n = int(input())
cnx = [[] for _ in range(n)]
for _ in range(n - 1):
    u, v, c = [int(i) for i in input().split()]
    cnx[u].append([v, c])
    cnx[v].append([u, c])


def cost(cur, src=-1):
    ans = 0
    for v, c in cnx[cur]:
        if v == src: continue
        ans = max(ans, c + cost(v, cur))
    return ans


ans = cost(0)
print(ans)
