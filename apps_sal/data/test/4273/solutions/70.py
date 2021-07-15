import itertools
from collections import defaultdict

n = int(input())
d = defaultdict(int)

for i in range(n):
    s = input()
    for e in ["M", "A", "R", "C", "H"]:
        if s[0] == e:
            d[e] += 1

sum_num = 0
l = ["M", "A", "R", "C", "H"]
for a, b, c in itertools.combinations(l, 3):
    sum_num += d[a] * d[b] * d[c]
print(sum_num)
