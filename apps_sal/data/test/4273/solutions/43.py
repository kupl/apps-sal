from collections import defaultdict
import itertools
n = int(input())
d = defaultdict(int)
for i in range(n):
    s = input()
    d[s[0]] += 1
l = ['M', 'A', 'R', 'C', 'H']
c = itertools.combinations(l, 3)
s = 0
for x in c:
    s += d[x[0]] * d[x[1]] * d[x[2]]
print(s)
