n, ma, mb = map(int, input().split())
al = []
bl = []
cl = []
for _ in range(n):
    a, b, c = map(int, input().split())
    al.append(a)
    bl.append(b)
    cl.append(c)
suma = sum(al)
MAX = 999999999999
gmincost = [MAX]


def dfsMa(id, count, sel):
    if id == n:
        return
    dfsMa(id + 1, count, sel)
    tempsum = al[id] + count
    bsum = costsum = 0
    for j in sel + [id]:
        bsum += bl[j]
        costsum += cl[j]
    if costsum > gmincost[0]:
        return
    elif tempsum % ma == 0:
        k = tempsum // ma
        if bsum == k * mb:
            gmincost[0] = min(gmincost[0], costsum)
            return
    dfsMa(id + 1, count + al[id], sel + [id])
    return


dfsMa(0, 0, [])
if gmincost[0] == MAX:
    print(-1)
else:
    print(gmincost[0])
