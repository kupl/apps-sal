from collections import deque
n, m = list(map(int, input().split()))
prefs = [{} for _ in range(n)]
cities = deque()
for i in range(m):
    p, y = list(map(int, input().split()))
    prefs[p - 1][y] = -1
    cities.append((p, y))

for p in prefs:
    years = list(p.keys())
    years.sort()
    for y in range(len(years)):
        p[years[y]] = y + 1


for _ in range(m):
    p, y = cities.popleft()
    cid = prefs[p - 1][y] + p * 1000000
    print(("{:0=12}".format(cid)))
