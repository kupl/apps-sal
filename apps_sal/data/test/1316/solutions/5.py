import itertools

n, k = list(map(int, input().split()))
s = input().strip()

resdict = {}
for c, g in itertools.groupby(s):
    count = len(list(g))
    if c not in resdict:
        resdict[c] = 0

    resdict[c] += count // k

print(max(resdict.values()))
