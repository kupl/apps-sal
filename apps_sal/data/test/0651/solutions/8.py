import itertools

n, m = [int(v) for v in input().split()]
l = [input() for _ in range(n)]
dirs = [int(c) for c in input()]

start, end = None, None
for i, line in enumerate(l):
    ps = line.find('S')
    pe = line.find('E')
    if ps != -1:
        start = (ps, i)
    if pe != -1:
        end = (pe, i)

# up, down, left, right
ways = [(0, -1), (0, 1), (-1, 0), (1, 0)]
cnt = 0

for p in itertools.permutations(list(range(4))):
    dst = [ways[pp] for pp in p]
    px, py = start
    for d in dirs:
        px += dst[d][0]
        py += dst[d][1]
        if px < 0 or px >= m or py < 0 or py >= n or l[py][px] == '#':
            break
        if (px, py) == end:
            cnt += 1
            break

print(cnt)
