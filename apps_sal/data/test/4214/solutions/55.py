from itertools import permutations

N = int(input())
XY = []
for _ in range(N):
    x, y = list(map(int, input().split()))
    XY.append((x, y))

ans = 0
c = 0

for p in permutations(list(range(N))):
    dist = 0
    x1, y1 = XY[p[0]]
    for i in p[1:]:
        x, y = XY[i]
        dist += ((x1 - x) ** 2 + (y1 - y) ** 2) ** 0.5
    ans += dist
    c += 1

print((ans / c))

