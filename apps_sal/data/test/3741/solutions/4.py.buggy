from collections import defaultdict

n = int(input())

arr = list(map(int, input().split()))

d = defaultdict(list)
dd = defaultdict(list)

for i, el in enumerate(arr):
    b = '{0:b}'.format(el)[::-1]
    for j, digit in enumerate(b):
        if digit == '1':
            for i2 in d[j]:
                dd[i].append(i2)
                dd[i2].append(i)
            d[j].append(i)
        if len(d[j]) == 3:
            print(3)
            return

colors = {i: [] for i in range(len(arr))}

min_cycle = float('+inf')

for i in range(len(arr)):
    if colors[i]:
        continue
    tier = [(i, [])]
    next_tier = []
    while tier:
        for t, way in tier:
            if colors[t]:
                c = 0
                while len(way) > c and len(colors[t]) > c and way[c] == \
                        colors[t][c]:
                    c += 1
                min_cycle = min(len(colors[t]) + len(way) - 2 * c + 1,
                                min_cycle)
                continue
            colors[t] = way + [t]
            for k in dd[t]:
                if (not way or k != way[-1]) and (k, colors[t]) not in next_tier:
                    next_tier.append((k, colors[t]))
        tier = next_tier
        next_tier = []

if min_cycle < 1e9:
    print(min_cycle)
else:
    print(-1)

pass
