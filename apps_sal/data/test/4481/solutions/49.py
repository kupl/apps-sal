import collections

N = int(input())
S = sorted([input() for _ in range(N)])

c = collections.Counter(S)

vmax = max(c.values())

for k, v in c.items():
    if v == vmax:
        print(k)
