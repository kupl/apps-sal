from pprint import pprint
import itertools
import collections
(n, m, k) = [int(s) for s in input().split()]
g = [[0] * m for _ in range(n)]
for i in range(n):
    r = input()
    for (j, c) in enumerate(r):
        if c == '.':
            g[i][j] = 1
sidecomps = set()
curlab = 1
labels = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if g[i][j] != 1 or labels[i][j] > 0:
            continue
        labels[i][j] = curlab
        stack = [(i, j)]
        if i == 0 or j == 0 or i == n - 1 or (j == m - 1):
            sidecomps.add(curlab)
        while stack:
            (i1, j1) = stack.pop()
            for (i2, j2) in [(i1 - 1, j1), (i1 + 1, j1), (i1, j1 - 1), (i1, j1 + 1)]:
                if 0 <= i2 and i2 < n and (0 <= j2) and (j2 < m) and (g[i2][j2] == 1) and (labels[i2][j2] == 0):
                    labels[i2][j2] = curlab
                    stack.append((i2, j2))
                    if i2 == 0 or j2 == 0 or i2 == n - 1 or (j2 == m - 1):
                        sidecomps.add(curlab)
        curlab += 1
lakes = collections.defaultdict(list)
for (i, j) in itertools.product(list(range(n)), list(range(m))):
    lab = labels[i][j]
    if lab > 0 and lab not in sidecomps:
        lakes[lab].append((i, j))
lakesizes = sorted(((len(lakes[lab]), lab) for lab in lakes))
num_remove = len(lakesizes) - k
ans = 0
for (_, lab) in lakesizes[:num_remove]:
    for (i, j) in lakes[lab]:
        g[i][j] = 0
        ans += 1
print(ans)
for i in range(n):
    print(''.join(('.' if g[i][j] else '*' for j in range(m))))
