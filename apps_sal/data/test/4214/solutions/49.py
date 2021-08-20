import itertools
from collections import defaultdict
N = int(input())
cities = [tuple(map(int, input().split())) for i in range(N)]
dist = defaultdict(int)
for perm in itertools.permutations(range(N), 2):
    (x1, y1) = cities[perm[0]]
    (x2, y2) = cities[perm[1]]
    dist[perm] = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
ans = 0
cnt = 0
for perm in itertools.permutations(range(N), N):
    cnt += 1
    for i in range(1, len(perm)):
        ans += dist[perm[i - 1], perm[i]]
print(ans / cnt)
