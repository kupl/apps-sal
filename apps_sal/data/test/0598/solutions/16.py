(n, x) = [int(x) for x in input().split()]

l_ind = [[] for i in range(200000)]
r_ind = [[] for i in range(200000)]

for i in range(n):
    (l, r, c) = [int(x) for x in input().split()]
    if r - l + 1 <= x:
        l_ind[l - 1].append((l, r, c))
        r_ind[r - 1].append((l, r, c))


ans = None

bestCost = [None for i in range(x + 1)]

for (vl, vr) in zip(l_ind, r_ind):
    for (l, r, c) in vl:
        cur_len = r - l + 1
        if bestCost[x - cur_len]:
            if ans:
                ans = min(ans, c + bestCost[x - cur_len])
            else:
                ans = c + bestCost[x - cur_len]
    for (l, r, c) in vr:
        cur_len = r - l + 1
        if bestCost[cur_len]:
            bestCost[cur_len] = min(bestCost[cur_len], c)
        else:
            bestCost[cur_len] = c


if ans == None:
    print(-1)
else:
    print(ans)

