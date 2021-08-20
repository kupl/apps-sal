(n, m) = [int(i) for i in input().split()]
hyou = []
for i in range(m):
    hyou.append([int(i) for i in input().split()])
next_island = set()
pre_island = set()
for go in hyou:
    (one, two) = go
    newone = min(one, two)
    newtwo = max(one, two)
    if newone == 1:
        next_island.add(newtwo)
    if newtwo == n:
        pre_island.add(newone)
ans = next_island & pre_island
if len(ans) == 0:
    print('IMPOSSIBLE')
else:
    print('POSSIBLE')
