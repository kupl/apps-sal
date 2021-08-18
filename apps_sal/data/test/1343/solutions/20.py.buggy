import sys

n, m, k = list(map(int, input().split()))

links = [[int(i) for i in input().split()] for i in range(m)]

if k == 0:
    print(-1)
    return

flour_cities = set(int(i) for i in input().split())

shortest_path = float('inf')
shortest_path_exists = False

for u, v, l in links:
    u_has_flour = u in flour_cities
    v_has_flour = v in flour_cities
    if (u_has_flour and not v_has_flour) or (not u_has_flour and v_has_flour):
        shortest_path_exists = True
        shortest_path = min(l, shortest_path)

if shortest_path_exists:
    print(shortest_path)
else:
    print(-1)
