import math

start = int(input())
costs = list(map(int, input().split()))
scosts = [(x + 1, costs[x]) for x in range(len(costs))]
scosts.sort(reverse=True)
mincost = scosts[0][1]
minnum = scosts[0][0]
for val, cost in scosts:
    if cost < mincost:
        mincost = cost
        minnum = val
best = [minnum for x in range(start // mincost)]
rem = start - (start // mincost) * mincost
for i in range(len(best)):
    changed = False
    for val, cost in scosts:
        if val > best[i] and (cost - mincost) <= rem:
            rem += mincost
            rem -= cost
            best[i] = val
            changed = True
            break
    if not changed:
        break
if len(best) == 0:
    print(-1)
else:
    ans = ""
    for val in best:
        ans += str(val)
    print(ans)
