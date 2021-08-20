import itertools
n = int(input())
lamps = input()
perms = itertools.permutations(['R', 'G', 'B'])
best = n
for p in perms:
    recolors = 0
    for i in range(n):
        if lamps[i] != p[i % 3]:
            recolors += 1
    if recolors < best:
        best = recolors
        bestp = p
print(best)
print(''.join(itertools.islice(itertools.cycle(bestp), n)))
