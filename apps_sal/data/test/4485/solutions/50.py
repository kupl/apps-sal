n, m = map(int,input().split())
init_island = set()
last_island = set()
for _ in range(m):
    a,b = map(int,input().split())
    a,b = min(a,b), max(a,b)
    if a == 1:
        init_island.add(b)
    elif b == n:
        last_island.add(a)
    else:
        continue
common = init_island.intersection(last_island)
if len(common) >= 1:
    print('POSSIBLE')
else:
    print('IMPOSSIBLE')
